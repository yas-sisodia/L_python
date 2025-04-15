from datetime import datetime
letter = ''' Dear <|Name|>,
           You are selected!
           <|Date|> '''

print(letter.replace("<|Name|>", "Yash").replace("<|Date|>", str(datetime.now().strftime("%d/%m/%Y"))))