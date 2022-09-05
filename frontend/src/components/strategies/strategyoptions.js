

export const strategyoptions = [
  {
    title: 'Home',
    url: './',
  },
  {
    title: 'Tracker',
    url: './Tracker',
    submenu: [
      {
        title: 'New',
        url: 'new',
      },
      {
        title: 'Active Trades',
        url: 'active-trades',
        submenu: [
          {
            title: 'Modify',
            url: 'modify',
          },
          {
            title: 'Cancel',
            url: 'cancel',
          },
        ],
      },
      {
        title: 'Check Status',
        url: 'status',
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