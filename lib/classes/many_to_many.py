class Article:
    #class variabe to store
    all = []
    def __init__(self, author, magazine, title):
        if not isinstance(title,str):
            raise Exception("Title must be of type string")
        
        if not (5 <= len(title) <= 50):
            raise Exception("Title must be between 5 and 50 characters")
        
        if not isinstance(author,Author):
            raise Exception("author must be a valid instance of class Author")
        
        if not isinstance(magazine,Magazine):
            raise Exception("magazine must be a valid instance of class Magazine")

        self.author = author
        self.magazine = magazine
        self._title = title
        magazine.add_article(self)
        Article.all.append(self)

        if self not in author._articles:
            author._articles.append(self)

    @property
    def title(self):
        return self._title
    
class Author:
    def __init__(self, name): 
        self.name = name  
        self._articles = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not isinstance(name, str): 
            raise Exception("Name must be a string.") 
        if len(name) == 0:
            raise Exception("Name must be longer than 0 characters")
        self._name = name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self,magazine,title)
        if article not in self._articles:
            self._articles.append(article)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles)) 

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise Exception("Name must be a string.")  
        
        if not (2 <= len(name) <= 16):
            raise Exception("Name must be between 2 and 16 characters,")
        
        if not isinstance(category, str): 
            raise Exception("Category must be a non-empty string.")  
        
        if len(category) == 0:
            raise Exception("Category must be longer than 0 characters")
        
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,new_name):
        if not isinstance(new_name, str):
            raise Exception("Name must be a string.")  
        
        if not (2 <= len(new_name) <= 16):
            raise Exception("Name must be between 2 and 16 characters,")
        
        self._name = new_name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self,new_category):
        if not isinstance(new_category, str):
            raise Exception("Category must be a string.")  
        
        if len(new_category) == 0:
            raise Exception("Category must be longer than 0 characters")
        
        self._category = new_category

    def add_article(self, article):  
        self._articles.append(article)  

    def articles(self):  
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles)) 
    
    
    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]
     
    
    # def contributing_authors(self):



author1 = Author("John")
author2 = Author("Brian")

tech_magazine = Magazine("TechTalk", "Technology")
food_magazine = Magazine("Foodies", "Culinary")


article1 = author1.add_article(tech_magazine, "The Rise of AI")
article2 = author1.add_article(food_magazine, "Fusion Cuisine Secrets")
article3 = author2.add_article(tech_magazine, "Quantum Computing Basics")


print(f"Author {author1.name}'s Articles: {[a.title for a in author1.articles()]}")
print(f"Author {author2.name}'s Articles: {[a.title for a in author2.articles()]}")
print(f"Magazines authored by {author1.name}: {[m.name for m in author1.magazines()]}")

print(f"{tech_magazine.name} Contributors: {[a.name for a in tech_magazine.contributors()]}")
print(f"{food_magazine.name} Article Titles: {food_magazine.article_titles()}")

print(f"Topics covered by {author1.name}: {author1.topic_areas()}")

try:
    invalid_article = author1.add_article(tech_magazine, "AI") 
except Exception as e:
    print(f"Error: {e}")

try:
    invalid_magazine = Magazine("S", "Tech")  
except Exception as e:
    print(f"Error: {e}")
