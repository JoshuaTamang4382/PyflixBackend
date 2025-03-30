# from django.db import models

# class Movie(models.Model):
#     movie_id = models.BigAutoField(primary_key=True)  # BigAutoField for large auto-incrementing ID
#     generes = [
#         ("action", "Action"),
#         ("comedy", "Comedy"),
#         ("drama", "Drama"),
#         ("horror", "Horror"),
#         ("romance", "Romance"),
#         ("thriller", "Thriller"),
#         ("documentary", "Documentary"),
#         # Add more categories as needed
#     ]

#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     release_date = models.DateField()
#     duration = models.PositiveIntegerField(help_text="Duration in minutes")
#     rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
#     image_url = models.URLField(max_length=500, blank=True, null=True)
#     video_url = models.URLField(max_length=500, blank=True, null=True)
#     categories = models.TextField(blank=True, default="")  # Store categories as a comma-separated string
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title

#     def set_categories(self, category_list):
#         """Helper function to set categories as a comma-separated string."""
#         self.categories = ",".join(category_list)

#     def get_categories(self):
#         """Helper function to get categories as a list."""
#         return self.categories.split(",") if self.categories else []


from django.db import models

class Movie(models.Model):
    movie_id = models.BigAutoField(primary_key=True)
    
    generes = [
        ("action", "Action"),
        ("comedy", "Comedy"),
        ("drama", "Drama"),
        ("horror", "Horror"),
        ("romance", "Romance"),
        ("thriller", "Thriller"),
        ("documentary", "Documentary"),
        # Add more categories as needed
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    
    # Image field for movie poster/image
    image = models.ImageField(upload_to='movies/images/', blank=True, null=True)
    
    # Video field for storing movie trailers or video files
    video = models.FileField(upload_to='movies/videos/', blank=True, null=True)
    
    categories = models.TextField(blank=True, default="")  # Store categories as a comma-separated string
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def set_categories(self, category_list):
        """Helper function to set categories as a comma-separated string."""
        self.categories = ",".join(category_list)

    def get_categories(self):
        """Helper function to get categories as a list."""
        return self.categories.split(",") if self.categories else []
