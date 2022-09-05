

export const navitems = [
    {
      title: 'Home',
      url: './',
    },
    {
      title: 'Tracker',
      url: './Tracker',
      submenu: [
        {
          title: 'web design',
          url: 'web-design',
        },
        {
          title: 'web development',
          url: 'web-dev',
          submenu: [
            {
              title: 'Frontend',
              url: 'frontend',
            },
            {
              title: 'Backend',
              submenu: [
                {
                  title: 'NodeJS',
                  url: 'node',
                },
                {
                  title: 'PHP',
                  url: 'php',
                },
              ],
            },
          ],
        },
        {
          title: 'SEO',
          url: 'seo',
        },
      ],
    },
    {
      title: 'About',
      url: './about',
      submenu: [
        {
          title: 'Who we are',
          url: 'who-we-are',
        },
        {
          title: 'Our values',
          url: 'our-values',
        },
      ],
    },
  ];