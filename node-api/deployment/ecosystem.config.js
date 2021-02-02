module.exports = {
  apps : [{
    name: 'movie-analyst-api',
    script: 'server.js',
    instances: 1,
    autorestart: true,
    watch: false,
    max_memory_restart: '1G',
    env: {
      NODE_ENV: 'production'
    },
    // env_production: {
    //   API_PORT: 3000,
    //   MYSQL_HOST: 'localhost',
    //   MYSQL_PORT: 3306,
    //   MYSQL_USER: 'movie',
	  //   MYSQL_PASSWORD: 'movie',
    //   MYSQL_DB_NAME: 'movie_db',
    // }
  }]
};
