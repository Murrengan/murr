/*
 *   Author:  Sergiej Selin
 *   Website: http://selin.com.pl
 *   Github:  https://github.com/selincodes
 *
 */
var gulp          = require('gulp'),
    sass          = require('gulp-sass'),
    browserSync   = require('browser-sync'),
    exec          = require('child_process').exec,
    cleancss      = require('gulp-clean-css'),
		rename        = require('gulp-rename'),
		autoprefixer  = require('gulp-autoprefixer'),
		concat        = require('gulp-concat'),
    notify        = require('gulp-notify');

var serverUrl     = 'localhost:8000',
    syntax        = 'scss', // Синтаксис: sass или scss
    gulpversion   = '4'; // Версия Gulp: 3 или 4


// Компиляция sass
gulp.task('styles', function() {
	return gulp.src('static/'+syntax+'/**/*.'+syntax+'')
	.pipe(sass({ outputStyle: 'expanded' }).on("error", notify.onError()))
	.pipe(concat('app.css'))
	.pipe(rename({ suffix: '.min', prefix : '' }))
	.pipe(autoprefixer(['last 15 versions']))
	.pipe(cleancss( {level: { 1: { specialComments: 0 } } }))
	.pipe(gulp.dest('static/css'))
	.pipe(browserSync.stream())
});

// Запуск django сервера
gulp.task('django', function() {
  var proc = exec('python manage.py runserver ' + serverUrl);
  proc.stderr.on('data', function(data) {
    process.stdout.write(data);
  });

  proc.stdout.on('data', function(data) {
    process.stdout.write(data);
  });
});

// Следим за изминениями html файлов
gulp.task('code', function() {
	return gulp.src('templates/**/*.html')
	.pipe(browserSync.reload({ stream: true }))
});

// Автообновление страницы
gulp.task('browser-sync', function () {
  browserSync.init({
		proxy: serverUrl,
		notify: false, // Убираем уведомления
		open: true, // Чтобы убрать автоматическое открытие в барузере, изменить на false
	});
});

if (gulpversion == 3) {
	gulp.task('watch', ['styles', 'django', 'browser-sync'], function() {
		gulp.watch('static/'+syntax+'/**/*.'+syntax+'', ['styles']);
		gulp.watch('templates/**/*.html', ['code'])
	});
	gulp.task('default', ['watch']);
}

if (gulpversion == 4) {
	gulp.task('watch', function() {
		gulp.watch('static/'+syntax+'/**/*.'+syntax+'', gulp.parallel('styles'));
		gulp.watch('templates/**/*.html', gulp.parallel('code'))
	});
	gulp.task('default', gulp.parallel('styles', 'django', 'browser-sync', 'watch'));
}