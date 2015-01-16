module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    uglify: {
      build: {
        src: [
          // bower components
            "bower_components/jquery/dist/jquery.js",
            'bower_components/bootstrap-sass-official/assets/bootstrap.js',
            'bower_components/scrollReveal.js/dist/scrollReveal.js',
            'bower_components/modernizr/modernizr.js',

          // internals
          // 'js/src/app.js',
          // 'js/src/filters.js',
          // 'js/src/utils.js',
          // 'js/src/controllers/*.js',
          // 'js/src/services/*.js'
        ],
        dest: 'js/app.min.js'
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-uglify');

  // Default task(s).
  grunt.registerTask('default', ['uglify']);

};