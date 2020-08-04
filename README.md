# Fun
Fun side-projects for sharing

The Secret Santa generator file (both notebook and .py files) uses functions that will take names and their respectives emails, pick their Secret Santa, end emails them. Comments in files are included. In order to let Python connect using your login info, one must access https://myaccount.google.com/security and turn on "Less secure app access". (Only works with Gmail, user can modify connection statements and port number in code if they wish to use email other than Gmail)

reg_fit.py is a small, useful file that will manipulate the x and y to create a regression line(s) based on the parameters.

NNFinalDraft.ipynb is a notebook that is essentially a MLP Classifier done by hand. This is a great exercise as it helps one understand what exactly goes on under the hood of a neural network. It is flexible on hidden layer sizes (but must have at least two hidden layers!!) It takes in an X, an encoded y, and original y for plotting purposes. 

passwordcracker.py is a simple password cracking function that returns the time it took to crack password as well as the number of guesses. Can be used to test safety of passwords.

"Password Cracker with Gradio Interface".ipynb is the same code as passwordcracker.py except the interfacing happens in a Gradio interface.

mnist_gradio.py is a code that creates an interactive sketchpad to predict the number drawn (digits 0-9 as the model was trained using the MNIST dataset).
 
