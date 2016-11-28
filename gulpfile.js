var gulp = require('gulp');
var concat = require('gulp-concat');
var rename = require('gulp-rename');
var uglify = require('gulp-uglify');

var jsDest = 'static/js';

gulp.task('storeScripts', function() {
    return gulp.src(['static/js/global.js', 'static/js/store.js'])
        .pipe(concat('allStore.js'))
        .pipe(rename('allStore.min.js'))
        .pipe(uglify())
        .pipe(gulp.dest(jsDest));
});

gulp.task('chatScripts', function() {
    return gulp.src(['static/js/global.js', 'static/js/chat.js'])
        .pipe(concat('allChat.js'))
        .pipe(rename('allChat.min.js'))
        .pipe(uglify())
        .pipe(gulp.dest(jsDest));
});

gulp.task('default', ['storeScripts', 'chatScripts']);
