

export const stockdataoptions = [
  {
    title: 'Home',
    url: '',
  },
  {
    title: 'Stock Data',
    url: 'stock-data',
    submenu: [
      {
        title: 'Price Info',
        url: 'price-info',
        submenu: [
          {
            title: 'LTP',
            url: 'ltp',
          },
          {
            title: 'Quotes',
            url: 'quotes',
          },
          {
            title: 'Market Depth',
            url: 'market-depth',
          },
        ],
      },
      {
        title: 'Price Chart',
        url: 'price-chart',
        submenu: [
          {
            title: 'Time Frame',
            url: 'timeframe',
          },
          {
            title: 'CPR',
            url: 'cpr',
          },
          {
            title: 'Camarilla',
            url: 'camarilla',
          },
        ],
      },
    ],
  },
  {
    title: 'Watch List',
    url: 'watchlist',
    submenu: [
      {
        title: 'Stock Tracker',
        url: 'stock-tracker',
      },
      {
        title: 'Price Mismatches',
        url: 'price-mismatch',
      },
    ],
  },
];