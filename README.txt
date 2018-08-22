###########################################################
**************TUTORIAL2: USING VIEWS IN FLASK**************
###########################################################

1. Create a sample webapp like before.
2. Go thru Blueprint documentation.
	Flask uses a concept of blueprints for making application components 
	and supporting common patterns within an application or across
	applications. Blueprints can greatly simplify how large applications
	work and provide a central means for Flask extensions to register 
	operations on applications. A Blueprint object works similarly to a 
	Flask application object, but it is not actually an application. 
	Rather it is a blueprint of how to construct or extend an application.	
	It is Modularization via blueprints.
 Each view in flask is a function, decorators can be used to inject additional
 functionalities.a decorator is a function that takes another function
 and extends the behavior of the latter function without explicitly 
 modifying it.
3. Templates>>Create a layout.html file
	in flask, you create templates that can inherit from each other.
4. Link your stylesheet in head of layout.html. <link rel,type,href={{some jinja stuff}}>
  you call the style.css file in the layout.html using href above. This is the jinja stuff
5. Next define your parameters in style.css file


##########################################################
Templates>>create index.html
views>>create index.py
6. add the blueprint template