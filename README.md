# RealTimeMarketDataVisualization

# Real-time Visualization of ETHBUSD Order Book and Trade Data on Binance Using Python

This repository contains two Python scripts that use the Binance API to create real-time visualizations of the ETHBUSD order book and trade data on the Binance exchange.

# ETHBUSD Order Book Visualization Script
The ethbusd_order_book.py script continuously updates and displays an order book for the ETHBUSD trading pair on Binance using the matplotlib library. The script fetches the order book data using the Binance API, computes the cumulative quantities and prices for each bid and ask level, and plots the bid and ask areas as area charts. The resulting plot provides a dynamic view of the current state of the ETHBUSD order book on Binance, which can be useful for monitoring market activity and identifying trends.

# ETHBUSD Trade Data Visualization Script
The ethbusd_trade_data.py script creates a real-time visualization of the ETHBUSD trade data on Binance using the Dash framework. The script fetches the trade data using the Binance API, and creates a scatter plot with the times on the x-axis, the prices on the y-axis, and the marker sizes and colors as specified. The resulting visualization updates every second with new trades and provides a dynamic view of the current state of the ETHBUSD trade data on Binance, which can be useful for monitoring market activity and identifying trends.

# Installation
Clone the repository to your local machine.
Install the required libraries: requests, json, numpy, matplotlib, collections, dash, dash_core_components, dash_html_components, and plotly.
Run either of the scripts using a Python interpreter.
Usage
To use the ethbusd_order_book.py script, simply run it using a Python interpreter. The script will continuously update and display the order book for the ETHBUSD trading pair on Binance using a matplotlib area chart.
To use the ethbusd_trade_data.py script, run it using a Python interpreter and open a web browser to the specified URL. The script will create a Dash app with a scatter plot of the trade data for the ETHBUSD trading pair on Binance, updating every second with new trades.

# Customization
The scripts can be easily customized for other trading pairs or exchanges by changing the API endpoints and symbols as needed.
The appearance and behavior of the visualizations can be customized using the libraries' various options and parameters.
Disclaimer
The scripts are provided as-is and are not intended for use in actual trading. The scripts are meant for educational and exploratory purposes only, and the accuracy and completeness of the data cannot be guaranteed. The scripts should be used at your own risk.
