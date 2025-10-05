# Quick Start Guide 🚀

## Nuclear Explosions Data Analysis

### For Beginners

#### Step 1: Setup Your Environment

1. Make sure you have Python 3.8+ installed:
```bash
python --version
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

#### Step 2: Run the Analysis

**Option A: Python Script (Recommended for quick results)**
```bash
python nuclear_analysis.py
```

This will:
- Print comprehensive statistics to your console
- Generate 4 PNG visualization files
- Take approximately 30-60 seconds to complete

**Option B: Jupyter Notebook (Recommended for interactive exploration)**
```bash
jupyter notebook nuclear_explosions_analysis.ipynb
```

Then:
1. Click "Cell" → "Run All" in the menu
2. Or press Shift+Enter to run cells one by one
3. Explore the interactive visualizations

#### Step 3: View Results

After running the script, check these files:
- `temporal_analysis.png` - Time-based trends
- `country_purpose_analysis.png` - Country comparisons
- `yield_analysis.png` - Explosion yields
- `geographic_analysis.png` - Test locations

### What You'll Learn

This analysis demonstrates:

1. **Data Loading & Exploration**
   - Reading CSV files with pandas
   - Checking data quality
   - Understanding dataset structure

2. **Statistical Analysis**
   - Descriptive statistics
   - Hypothesis testing
   - Correlation analysis

3. **Data Visualization**
   - Line plots for trends
   - Bar charts for comparisons
   - Scatter plots for distributions
   - Heatmaps for relationships
   - Pie charts for proportions

4. **Time Series Analysis**
   - Yearly trends
   - Decade patterns
   - Cumulative analysis

5. **Categorical Analysis**
   - Country comparisons
   - Purpose classification
   - Type distributions

### Key Questions Answered

- 📊 How many nuclear explosions occurred?
- 🌍 Which countries conducted the most tests?
- 📅 When was nuclear testing at its peak?
- 💥 What were the largest explosions?
- 🎯 What were the purposes of these tests?
- 📉 How did testing change over time?
- 🗺️ Where were tests conducted?

### Troubleshooting

**Issue: ModuleNotFoundError**
```bash
# Solution: Install missing packages
pip install pandas numpy matplotlib seaborn scipy
```

**Issue: CSV file not found**
```bash
# Solution: Make sure you're in the correct directory
cd Nuclear-Explosions-Analysis
ls nuclear_explosions.csv  # Should show the file
```

**Issue: Jupyter notebook won't open**
```bash
# Solution: Install Jupyter
pip install jupyter
```

### Next Steps

After completing this analysis:

1. **Modify the code** - Try changing visualization styles
2. **Add new analysis** - Explore different aspects of the data
3. **Create your own insights** - Look for patterns we might have missed
4. **Share your findings** - Create a blog post or presentation

### Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)

### Need Help?

- Check the main README.md for detailed information
- Review the code comments in nuclear_analysis.py
- Explore the Jupyter notebook step-by-step

---

Happy analyzing! 📊🔬
