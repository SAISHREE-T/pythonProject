import streamlit as stl
import math as mt
stl.title("Welcome to my simple calculator!")
op=stl.selectbox("Select an operation",["Addition","Subtraction","Multiplication","Division","Power of number","Logarithm","Square root"])

if op=="Addition"or op=="Subtraction" or op=="Multiplication"or op=="Division":
    num1=stl.number_input("Enter the first number")
    num2=stl.number_input("Enter the second number",value=1)
    if op=="Addition":
        result=num1+num2
    elif op=="Subtraction":
        result=num1-num2
    elif op=="Multiplication":
        result=num1*num2
    elif op=="Division":
        if num2!=0:
            result=num1/num2
        else:
            result="ERROR! Division by 0 is not possible"
elif op=="Power of number":
    base=stl.number_input("Enter the base")
    power=stl.number_input("Enter the power")
    result=mt.pow(base,power)
elif op=="Logarithm":
    num1=stl.number_input("Enter the number",value=1)
    base=stl.number_input("Enter the base",value=10)
    result=mt.log(num1,base)
elif op=="Square root":
    num1=stl.number_input("Enter the number")
    result=mt.sqrt(num1)

stl.write(f"The result is {result} ")
#To run it, you can open a terminal  and navigate to the directory where your script is located. Then, run the following command:
# streamlit run <name_of_script>
# This command will start a local development server, and it should automatically open a new tab in your default web browser displaying your Streamlit app.
