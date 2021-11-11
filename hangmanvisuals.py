def guess_one(wrong_guesses):

        if wrong_guesses == 0:
            print("""
            ==================
            """)

        if wrong_guesses == 1:
            print("""
                    |
                    |        
                    |        
                    |       
                    |       
                    |
            ==================
            """)

        if wrong_guesses == 2:
            print("""
                    |---------
                    |        
                    |          
                    |       
                    |       
                    |
            ==================
            """)

        if wrong_guesses == 3:
            print("""
                    |---------
                    |        |
                    |        
                    |       
                    |       
                    |
            ==================
            """)

        if wrong_guesses == 4:
            print("""
                    |---------
                    |        |
                    |        O    
                    |       
                    |       
                    |
            ==================
            """)

        if wrong_guesses == 5:
            print("""
                    |---------
                    |        |
                    |        O    
                    |        |
                    |       
                    |
            ==================
            """)

        if wrong_guesses == 6:
            print("""
                    |---------
                    |        |
                    |        O    
                    |       /|
                    |       
                    |
            ==================
            """)

        # r treats \ as just a character
        if wrong_guesses == 7:
            print(r"""
                    |---------
                    |        |
                    |        O    
                    |       /|\
                    |       
                    |
            ==================
            """)

        if wrong_guesses == 8:
            print(r"""
                    |---------
                    |        |
                    |        O    
                    |       /|\
                    |       / 
                    |
            ==================
            """)

        if wrong_guesses == 9:
            print(r"""
                    |---------
                    |        |
                    |        O    
                    |       /|\
                    |       / \
                    |
            ==================
            """)
