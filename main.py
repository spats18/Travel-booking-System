from website import create_app # we can do this bec now our website is a package because of init file

app = create_app()

if __name__ == '__main__':
    app.run(debug = True) # debug = True will automatically rerun our website if we did any change in the code. 
    #will turn it off in production