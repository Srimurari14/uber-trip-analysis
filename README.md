# Uber Trip Analysis

## Overview
Since it was founded in 2009, Uber has become one of the most famous unicorn companies, offering its services to more than 80 countries worldwide. This Python project for beginners aims to analyze Uber rides to detect specific patterns, such as the busiest day or the time with the lowest number of rides. 

## Dataset
- **Source**: Uber raw trip data for September 2014.
- **Format**: CSV file with fields such as `Date/Time`, `Lat`, `Lon`, and `Base`.

## Objectives
1. Explore the dataset and understand its structure.
2. Analyze ride patterns by:
   - Location (latitude and longitude).
   - Time (hourly, daily, and weekly trends).
   - Base code usage.
3. Visualize the data using Python's `matplotlib` library.

## Features
- **Exploratory Data Analysis**:
  - Inspected data shape, head, tail, and statistical summary.
  - Checked for missing values and their proportions.
- **Derived Features**:
  - Extracted `Day`, `Hour`, and `Weekday` from the `Date/Time` column.
- **Visualizations**:
  - Scatter plots for ride locations.
  - Histograms for rides per day, hour, and weekday.
  - Bar charts for base usage frequencies.

## Technologies Used
- **Python**: Main programming language.
- **Libraries**:
  - `pandas` for data manipulation and analysis.
  - `matplotlib` for creating visualizations.
