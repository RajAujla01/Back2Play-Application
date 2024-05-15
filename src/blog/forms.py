from django import forms

from blog.models import BlogPost

class CreateBlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost                    #model form after BlogPost model 
        fields = ['title', 'body', 'image'] #fields for form 


class UpdateBlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image']
        
    def save(self, commit=True):                            #only called if commit is set to true                
        blog_post = self.instance                           #get blog post 
        blog_post.title = self.cleaned_data['title']        #reference the title, body and image 
        blog_post.body = self.cleaned_data['body']

        if self.cleaned_data['image']:
            blog_post.image = self.cleaned_data['image']    
        
        if commit:
            blog_post.save()                                #save the blog post changes 

        return blog_post                                    #return the saved blog post 
    
