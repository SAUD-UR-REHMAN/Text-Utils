from django.http import HttpResponse
from django.shortcuts import render

''' Show the Index/Home page'''

def index(request):
    return render(request,'index.html')


''' Analizing text for different utilities '''

def analize(request):
    #### getting the text and the check values ####
    text=request.POST.get('user_text','default')
    punc_check=request.POST.get('punc','off')
    new_line_check=request.POST.get('new_line','off')
    cap_check=request.POST.get('caps','off')
    char_count=request.POST.get('char_count','off')
    char_count_text=request.POST.get('count','off')
    lower_check=request.POST.get('lower','off')
    titel_check=request.POST.get('titel','off')
    space_check=request.POST.get('space','off')


    #### Removing punctuation from text ####
    if punc_check == "on":
        analized = ""
        punc_list='''`~!'"?^%$#@^&*()><.;-_\|/,:+'''
        for char in text:
            if char not in punc_list:
                analized = analized + char
        para={'work':'Removes the Punctuations of text','analized_text' : analized}
        return render(request,'punctuation.html',para)

    #### Removing new_line the text ####
    elif(new_line_check=="on"):
        analized = ""
        for char in text:
            if char != "\n" and char != "\r":
                analized = analized + char
        para={'work':'Removed new lines from your text','analized_text' : analized}
        return render(request,'punctuation.html',para)


    #### Capitalizing The Text ####
    elif (cap_check == "on"):
        analized = ""
        for char in text:
            analized = analized + char.capitalize()
        para = {'work': 'Capitalized your text', 'analized_text': analized}
        return render(request, 'punctuation.html', para)

    #### Lower Case The Text ####
    elif (lower_check == "on"):
        analized = ""
        for char in text:
            analized = analized + char.lower()
        para = {'work': 'Capitalized your text', 'analized_text': analized}
        return render(request, 'punctuation.html', para)

    ####  Titel Case The Text ####
    elif (titel_check == "on"):
        analized = text.title()
        para = {'work': 'Capitalized your text', 'analized_text': analized}
        return render(request, 'punctuation.html', para)

    #### Characters count ####
    elif (char_count == "on"):
        txt = char_count_text
        analized = text.count(txt)
        para = {'work': 'counts your given char in the string', 'analized_text': analized}
        return render(request, 'punctuation.html', para)

    #### Extra space remove ####
    elif (space_check == "on"):
        analized = ""
        for index,char in enumerate(text):
            if not(text[index] == " " and text[index+1] == " "):
                analized = analized + char
        para = {'work': 'Removes Extra Spaces from your text', 'analized_text': analized}
        return render(request, 'punctuation.html', para)



    #### ERROR will we shown if no option is choosed ####

    else:

        return HttpResponse('''
        <!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Text Utils</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
</head>
<body>


<!--TOP NAV BAR START-->
<nav class="navbar navbar-expand-lg py-3 fixed-top" style="background-color: dodgerblue; color:white;">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">TEXTUTILS</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup"
                aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div class="navbar-nav">
                <a class="nav-link active" aria-current="page" href="#">Home</a>
                <a class="nav-link" href="#">About Us</a>
                <a class="nav-link" href="#">Contact Us</a>
            </div>
        </div>
        <form class="d-flex" role="search">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
    </div>
</nav>
<!--TOP NAV BAR ENDS-->

<!--marquee starts-->
<marquee behavior=""  direction="left" class="bg-info py-3">This website can make changes to your text as per your need.
    Your can play with your text as you want
</marquee>
<!--marquee ends-->
         
   <div class="modal" style="display:inline-table" tabindex="-1" role="dialog">
  <div class="modal-dialog" style="height: 100vh !important; display: flex;" role="document">
    <div class="modal-content" style="margin: auto !important; height: fit-content !important;">
      <div class="modal-header">
        <h5 class="modal-title">ERROR---></h5>
        
      </div>
      <div class="modal-body">
        <p>Did you forget to click one of the chack boxes, then plz click one...</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary"><a href="http://127.0.0.1:8000/" style="all:unset;"> Back to TextUtils </a></button>
      </div>
    </div>
  </div>
</div>
 
 
 <!--footer starts-->

<div class="container-fluid" style="position: fixed;bottom: 0;width: 100%;">
    <div class="row text-center py-2 bg-dark text-white"><strong>CopyRight 2022</strong></div>

</div>

<!--footer ends-->
 
 <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2"
        crossorigin="anonymous">
</script>
</body>
</html>
 ''')