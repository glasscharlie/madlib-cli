from madlib import print_intro

def test_index_one():
    expected =  "**************************************"
    "**        Welcome to Madlibs!       **"
    "**************************************"
    "** You will be prompted for a list  **"
    "**      of words to substitute      **"
    "**     for blanks in the story      **"
    "**************************************"
    actual = print_intro()  
    assert actual == expected