import cairo 
import math
  
def arrow(context, x, y, width, height, a, b): 
    context.move_to(x, y + b) 
    context.line_to(x, y + height - b) 
    context.line_to(x + a, y + height - b) 
    context.line_to(x + a, y + height) 
    context.line_to(x + width, y + height/2) 
    context.line_to(x + a, y) 
    context.line_to(x + a, y + b) 
    context.close_path() 


with cairo.SVGSurface("geek95.svg", 700, 700) as surface: 
    
    context = cairo.Context(surface) 
  
    context.set_source_rgb(0, 0, 0.5) 
    
    arrow(context, 20, 20, 150, 150, 75, 50) 
    
    context.fill() 
  
    
    arrow(context, 220, 20, 150, 150, 50, 30) 
    
    context.fill() 
    
    arrow(context, 420, 20, 150, 150, 25, 20) 
    
    context.fill() 
    
    arrow(context, 70, 220, 75, 150, 0, 50) 
    
    context.fill() 
   
  
with cairo.SVGSurface("geek1.svg", 700, 700) as surface: 
      
    
    context = cairo.Context(surface) 
      
    
    context.rectangle(50, 50, 100, 100) 
      
    
    context.rectangle(200, 200, 100, 50) 
      
    
    context.stroke() 
      
    
    context.arc(330, 60, 40, 500, 2*22/7) 
      
     
    context.stroke() 
     
     
    context.arc(500, 60, 40, 0, 2*22/7) 
      
      
    
    context.scale(700, 700) 
      
    
    context.set_line_width(0.0025) 
      
     
    context.set_source_rgba(0, 0, 0, 1) 
      
    

    context.set_source_rgb(0.6, 0.6, 0.6)

    context.rectangle(20, 20, 120, 80)
    context.rectangle(180, 20, 80, 80)
    context.fill()

    context.arc(330, 60, 40, 0, 2*math.pi)
    context.fill()
    
    context.arc(90, 160, 40, math.pi/4, math.pi)
    context.fill()

    context.translate(220, 180)
    context.scale(1, 0.7)
    context.arc(0, 0, 50, 0, 2*math.pi)
    context.fill()
    context.stroke() 

     
  
print("File Saved") 
