"""
Nuclear Explosions Analysis
A comprehensive data analysis of nuclear explosions worldwide (1945-1998)

This script performs exploratory data analysis, statistical analysis,
and generates visualizations for the nuclear explosions dataset.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")


def load_and_explore_data(filepath='nuclear_explosions.csv'):
    """Load and perform initial exploration of the dataset."""
    print("=" * 80)
    print("NUCLEAR EXPLOSIONS DATA ANALYSIS")
    print("=" * 80)
    
    # Load data
    df = pd.read_csv(filepath)
    
    print("\n1. DATASET OVERVIEW")
    print("-" * 80)
    print(f"Total number of nuclear explosions: {len(df)}")
    print(f"Time period: {df['Date.Year'].min()} - {df['Date.Year'].max()}")
    print(f"\nDataset shape: {df.shape}")
    print(f"Columns: {df.shape[1]}")
    
    print("\n2. COLUMN INFORMATION")
    print("-" * 80)
    print(df.dtypes)
    
    print("\n3. MISSING VALUES")
    print("-" * 80)
    missing = df.isnull().sum()
    if missing.sum() > 0:
        print(missing[missing > 0])
    else:
        print("No missing values found!")
    
    print("\n4. BASIC STATISTICS")
    print("-" * 80)
    print(df.describe())
    
    return df


def analyze_by_country(df):
    """Analyze nuclear explosions by country."""
    print("\n" + "=" * 80)
    print("COUNTRY-WISE ANALYSIS")
    print("=" * 80)
    
    country_counts = df['Location.Country'].value_counts()
    print("\nNuclear explosions by country:")
    print(country_counts)
    
    print(f"\nTotal countries with nuclear explosions: {len(country_counts)}")
    
    # Calculate total yield by country
    df['Average.Yield'] = (df['Data.Yeild.Lower'] + df['Data.Yeild.Upper']) / 2
    country_yield = df.groupby('Location.Country')['Average.Yield'].agg(['sum', 'mean', 'max'])
    country_yield = country_yield.sort_values('sum', ascending=False)
    
    print("\nTotal yield by country (kilotons):")
    print(country_yield)
    
    return country_counts, country_yield


def analyze_temporal_trends(df):
    """Analyze temporal trends in nuclear explosions."""
    print("\n" + "=" * 80)
    print("TEMPORAL ANALYSIS")
    print("=" * 80)
    
    # Explosions by year
    yearly_counts = df.groupby('Date.Year').size()
    print("\nExplosions per year (first 10 years and last 10 years):")
    print("First 10 years:")
    print(yearly_counts.head(10))
    print("\nLast 10 years:")
    print(yearly_counts.tail(10))
    
    # Peak year
    peak_year = yearly_counts.idxmax()
    peak_count = yearly_counts.max()
    print(f"\nPeak year: {peak_year} with {peak_count} explosions")
    
    # Decade analysis
    df['Decade'] = (df['Date.Year'] // 10) * 10
    decade_counts = df.groupby('Decade').size()
    print("\nExplosions by decade:")
    print(decade_counts)
    
    return yearly_counts, decade_counts


def analyze_purpose_and_type(df):
    """Analyze the purpose and type of nuclear explosions."""
    print("\n" + "=" * 80)
    print("PURPOSE AND TYPE ANALYSIS")
    print("=" * 80)
    
    # Purpose analysis
    purpose_counts = df['Data.Purpose'].value_counts()
    print("\nExplosions by purpose:")
    print(purpose_counts)
    
    # Type analysis
    type_counts = df['Data.Type'].value_counts()
    print("\nExplosions by type:")
    print(type_counts)
    
    return purpose_counts, type_counts


def analyze_yield(df):
    """Analyze the yield of nuclear explosions."""
    print("\n" + "=" * 80)
    print("YIELD ANALYSIS")
    print("=" * 80)
    
    df['Average.Yield'] = (df['Data.Yeild.Lower'] + df['Data.Yeild.Upper']) / 2
    
    print("\nYield statistics (kilotons):")
    print(f"Mean yield: {df['Average.Yield'].mean():.2f}")
    print(f"Median yield: {df['Average.Yield'].median():.2f}")
    print(f"Maximum yield: {df['Average.Yield'].max():.2f}")
    print(f"Minimum yield: {df['Average.Yield'].min():.2f}")
    print(f"Standard deviation: {df['Average.Yield'].std():.2f}")
    
    # Largest explosions
    print("\nTop 10 largest nuclear explosions:")
    largest = df.nlargest(10, 'Average.Yield')[['Data.Name', 'Location.Country', 
                                                   'Date.Year', 'Average.Yield']]
    print(largest.to_string(index=False))
    
    # Yield categories
    df['Yield.Category'] = pd.cut(df['Average.Yield'], 
                                   bins=[0, 20, 150, 1000, np.inf],
                                   labels=['Low (<20kt)', 'Medium (20-150kt)', 
                                          'High (150-1000kt)', 'Very High (>1000kt)'])
    yield_categories = df['Yield.Category'].value_counts().sort_index()
    print("\nExplosions by yield category:")
    print(yield_categories)
    
    return df


def create_visualizations(df, yearly_counts, country_counts, purpose_counts, 
                         type_counts, decade_counts):
    """Create comprehensive visualizations."""
    print("\n" + "=" * 80)
    print("GENERATING VISUALIZATIONS")
    print("=" * 80)
    
    # Figure 1: Temporal trends
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Nuclear Explosions: Temporal Analysis', fontsize=16, fontweight='bold')
    
    # Subplot 1: Yearly trend
    axes[0, 0].plot(yearly_counts.index, yearly_counts.values, marker='o', linewidth=2)
    axes[0, 0].set_xlabel('Year', fontsize=12)
    axes[0, 0].set_ylabel('Number of Explosions', fontsize=12)
    axes[0, 0].set_title('Nuclear Explosions Over Time', fontsize=14)
    axes[0, 0].grid(True, alpha=0.3)
    
    # Subplot 2: Decade distribution
    axes[0, 1].bar(decade_counts.index.astype(str), decade_counts.values, color='coral')
    axes[0, 1].set_xlabel('Decade', fontsize=12)
    axes[0, 1].set_ylabel('Number of Explosions', fontsize=12)
    axes[0, 1].set_title('Nuclear Explosions by Decade', fontsize=14)
    axes[0, 1].tick_params(axis='x', rotation=45)
    
    # Subplot 3: Country-wise yearly trend
    top_countries = country_counts.head(5).index
    for country in top_countries:
        country_yearly = df[df['Location.Country'] == country].groupby('Date.Year').size()
        axes[1, 0].plot(country_yearly.index, country_yearly.values, 
                       marker='o', label=country, linewidth=2)
    axes[1, 0].set_xlabel('Year', fontsize=12)
    axes[1, 0].set_ylabel('Number of Explosions', fontsize=12)
    axes[1, 0].set_title('Top 5 Countries: Yearly Trends', fontsize=14)
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)
    
    # Subplot 4: Cumulative explosions
    cumulative = yearly_counts.cumsum()
    axes[1, 1].fill_between(cumulative.index, cumulative.values, alpha=0.7, color='skyblue')
    axes[1, 1].plot(cumulative.index, cumulative.values, color='navy', linewidth=2)
    axes[1, 1].set_xlabel('Year', fontsize=12)
    axes[1, 1].set_ylabel('Cumulative Explosions', fontsize=12)
    axes[1, 1].set_title('Cumulative Nuclear Explosions', fontsize=14)
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('temporal_analysis.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: temporal_analysis.png")
    plt.close()
    
    # Figure 2: Country and Purpose Analysis
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Nuclear Explosions: Country and Purpose Analysis', fontsize=16, fontweight='bold')
    
    # Subplot 1: Country distribution
    top_10_countries = country_counts.head(10)
    axes[0, 0].barh(range(len(top_10_countries)), top_10_countries.values, color='steelblue')
    axes[0, 0].set_yticks(range(len(top_10_countries)))
    axes[0, 0].set_yticklabels(top_10_countries.index)
    axes[0, 0].set_xlabel('Number of Explosions', fontsize=12)
    axes[0, 0].set_title('Top 10 Countries by Number of Explosions', fontsize=14)
    axes[0, 0].invert_yaxis()
    
    # Subplot 2: Purpose distribution
    axes[0, 1].pie(purpose_counts.values, labels=purpose_counts.index, autopct='%1.1f%%',
                   startangle=90, textprops={'fontsize': 10})
    axes[0, 1].set_title('Distribution by Purpose', fontsize=14)
    
    # Subplot 3: Type distribution
    axes[1, 0].pie(type_counts.values, labels=type_counts.index, autopct='%1.1f%%',
                   startangle=90, textprops={'fontsize': 9})
    axes[1, 0].set_title('Distribution by Explosion Type', fontsize=14)
    
    # Subplot 4: Country vs Purpose heatmap
    country_purpose = pd.crosstab(df['Location.Country'], df['Data.Purpose'])
    top_countries_heatmap = country_counts.head(8).index
    country_purpose_subset = country_purpose.loc[top_countries_heatmap]
    sns.heatmap(country_purpose_subset, annot=True, fmt='d', cmap='YlOrRd', 
                ax=axes[1, 1], cbar_kws={'label': 'Count'})
    axes[1, 1].set_title('Country vs Purpose Heatmap', fontsize=14)
    axes[1, 1].set_xlabel('Purpose', fontsize=12)
    axes[1, 1].set_ylabel('Country', fontsize=12)
    
    plt.tight_layout()
    plt.savefig('country_purpose_analysis.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: country_purpose_analysis.png")
    plt.close()
    
    # Figure 3: Yield Analysis
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Nuclear Explosions: Yield Analysis', fontsize=16, fontweight='bold')
    
    # Subplot 1: Yield distribution (log scale)
    axes[0, 0].hist(df['Average.Yield'], bins=50, color='orange', edgecolor='black', alpha=0.7)
    axes[0, 0].set_xlabel('Yield (kilotons)', fontsize=12)
    axes[0, 0].set_ylabel('Frequency', fontsize=12)
    axes[0, 0].set_title('Distribution of Explosion Yields', fontsize=14)
    axes[0, 0].set_yscale('log')
    
    # Subplot 2: Yield by country (top 5)
    top_5_countries = country_counts.head(5).index
    country_yields = [df[df['Location.Country'] == country]['Average.Yield'].values 
                     for country in top_5_countries]
    axes[0, 1].boxplot(country_yields, labels=top_5_countries)
    axes[0, 1].set_ylabel('Yield (kilotons)', fontsize=12)
    axes[0, 1].set_title('Yield Distribution by Top 5 Countries', fontsize=14)
    axes[0, 1].set_yscale('log')
    axes[0, 1].tick_params(axis='x', rotation=45)
    
    # Subplot 3: Yield over time
    yearly_avg_yield = df.groupby('Date.Year')['Average.Yield'].mean()
    axes[1, 0].scatter(df['Date.Year'], df['Average.Yield'], alpha=0.3, s=10)
    axes[1, 0].plot(yearly_avg_yield.index, yearly_avg_yield.values, 
                   color='red', linewidth=2, label='Average')
    axes[1, 0].set_xlabel('Year', fontsize=12)
    axes[1, 0].set_ylabel('Yield (kilotons)', fontsize=12)
    axes[1, 0].set_title('Yield Over Time', fontsize=14)
    axes[1, 0].set_yscale('log')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)
    
    # Subplot 4: Yield categories
    yield_categories = df['Yield.Category'].value_counts()
    axes[1, 1].bar(range(len(yield_categories)), yield_categories.values, 
                  color=['green', 'yellow', 'orange', 'red'])
    axes[1, 1].set_xticks(range(len(yield_categories)))
    axes[1, 1].set_xticklabels(yield_categories.index, rotation=45, ha='right')
    axes[1, 1].set_ylabel('Number of Explosions', fontsize=12)
    axes[1, 1].set_title('Explosions by Yield Category', fontsize=14)
    
    plt.tight_layout()
    plt.savefig('yield_analysis.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: yield_analysis.png")
    plt.close()
    
    # Figure 4: Geographic Analysis
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    fig.suptitle('Nuclear Explosions: Geographic Distribution', fontsize=16, fontweight='bold')
    
    # Subplot 1: Scatter plot of locations
    for country in country_counts.head(5).index:
        country_data = df[df['Location.Country'] == country]
        axes[0].scatter(country_data['Location.Cordinates.Longitude'], 
                       country_data['Location.Cordinates.Latitude'],
                       alpha=0.6, s=50, label=country)
    axes[0].set_xlabel('Longitude', fontsize=12)
    axes[0].set_ylabel('Latitude', fontsize=12)
    axes[0].set_title('Geographic Distribution of Tests (Top 5 Countries)', fontsize=14)
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # Subplot 2: Regional distribution
    region_counts = df['Location.Region'].value_counts().head(15)
    axes[1].barh(range(len(region_counts)), region_counts.values, color='teal')
    axes[1].set_yticks(range(len(region_counts)))
    axes[1].set_yticklabels(region_counts.index, fontsize=10)
    axes[1].set_xlabel('Number of Explosions', fontsize=12)
    axes[1].set_title('Top 15 Test Regions', fontsize=14)
    axes[1].invert_yaxis()
    
    plt.tight_layout()
    plt.savefig('geographic_analysis.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: geographic_analysis.png")
    plt.close()
    
    print("\nAll visualizations generated successfully!")


def generate_key_insights(df, country_counts, yearly_counts):
    """Generate key insights from the analysis."""
    print("\n" + "=" * 80)
    print("KEY INSIGHTS & FINDINGS")
    print("=" * 80)
    
    insights = []
    
    # Total explosions
    insights.append(f"1. Total nuclear explosions recorded: {len(df)}")
    
    # Time period
    insights.append(f"2. Time period: {df['Date.Year'].min()} to {df['Date.Year'].max()} ({df['Date.Year'].max() - df['Date.Year'].min()} years)")
    
    # Countries
    insights.append(f"3. Number of countries conducting tests: {df['Location.Country'].nunique()}")
    insights.append(f"4. Top 3 countries: {', '.join([f'{c} ({country_counts[c]})' for c in country_counts.head(3).index])}")
    
    # Peak activity
    peak_year = yearly_counts.idxmax()
    insights.append(f"5. Peak year of testing: {peak_year} with {yearly_counts[peak_year]} explosions")
    
    # Cold War era
    cold_war_tests = df[(df['Date.Year'] >= 1947) & (df['Date.Year'] <= 1991)]
    insights.append(f"6. Cold War era tests (1947-1991): {len(cold_war_tests)} ({len(cold_war_tests)/len(df)*100:.1f}% of all tests)")
    
    # Post-Cold War
    post_cold_war = df[df['Date.Year'] > 1991]
    insights.append(f"7. Post-Cold War tests (1992+): {len(post_cold_war)}")
    
    # Yield insights
    insights.append(f"8. Average yield: {df['Average.Yield'].mean():.2f} kilotons")
    insights.append(f"9. Largest explosion: {df['Average.Yield'].max():.2f} kilotons ({df.loc[df['Average.Yield'].idxmax(), 'Data.Name']})")
    
    # Purpose
    top_purpose = df['Data.Purpose'].value_counts().index[0]
    insights.append(f"10. Most common purpose: {top_purpose} ({df['Data.Purpose'].value_counts()[top_purpose]} tests)")
    
    # Type
    top_type = df['Data.Type'].value_counts().index[0]
    insights.append(f"11. Most common type: {top_type} ({df['Data.Type'].value_counts()[top_type]} tests)")
    
    # Combat usage
    combat_tests = df[df['Data.Purpose'] == 'Combat']
    insights.append(f"12. Combat usage: {len(combat_tests)} explosions (Hiroshima and Nagasaki)")
    
    for insight in insights:
        print(insight)
    
    return insights


def main():
    """Main execution function."""
    # Load and explore data
    df = load_and_explore_data()
    
    # Perform analyses
    country_counts, country_yield = analyze_by_country(df)
    yearly_counts, decade_counts = analyze_temporal_trends(df)
    purpose_counts, type_counts = analyze_purpose_and_type(df)
    df = analyze_yield(df)
    
    # Generate key insights
    insights = generate_key_insights(df, country_counts, yearly_counts)
    
    # Create visualizations
    create_visualizations(df, yearly_counts, country_counts, purpose_counts, 
                         type_counts, decade_counts)
    
    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETE!")
    print("=" * 80)
    print("\nGenerated files:")
    print("  - temporal_analysis.png")
    print("  - country_purpose_analysis.png")
    print("  - yield_analysis.png")
    print("  - geographic_analysis.png")
    print("\nThank you for using Nuclear Explosions Analysis Tool!")


if __name__ == "__main__":
    main()
