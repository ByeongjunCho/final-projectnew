from django.shortcuts import render,redirect,get_object_or_404
from .forms import MovieForm,ReviewForm
from .models import Movie,Review, Genre
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    # bmovies = BMovie.objects.all()
    context = {
        'movies':movies,
        # 'bmovies': bmovies,
    }
    for i, v in enumerate(genres):
        context.update({'genre'+str(i) : v})
    return render(request,'movies/index.html',context)

def detail(request,movie_id):
    movie = get_object_or_404(Movie,id=movie_id)
    reviews = Review.objects.filter(movie_id=movie.pk)
    review_form = ReviewForm()
    context = {
        'reviews':reviews,
        'movie':movie,
        'review_form':review_form,
    }
    return render(request,'movies/detail.html',context)

@login_required
def review_create(request,movie_id):
    movie = get_object_or_404(Movie,id=movie_id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.movie_id = movie
            # review.user_id = request.user
            review.save()
            return redirect('movies:detail',movie_id)

def review_delete(request,movie_id,review_id):
    review = Review.objects.get(id=review_id)
    review.delete()
    return redirect('movies:detail',movie_id)


@login_required
def like(request,movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    if request.user in movie.like_users.all():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    return redirect('movies:detail',movie_id)
