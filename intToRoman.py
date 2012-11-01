''' This function convert integers to roman numerals '''
import string
romanPattern = {
    '1' : ('I','IV','V','IX'),
    '2' : ('X','XL','L','LC'),
    '3' : ('C','CD','D','CM'),
    '4' : ('M')
   }

def intToRoman(num):
    while num>=1 and num<=3999:
        (th_d, th_mod) = divmod(num,1000)#check for thoudands
        if th_d >=1 and th_d <=3:
            th_r = romanPattern['4']*th_d
            print th_r
            
        (hun_d, hun_mod) = divmod(th_mod,100)#check the hundredse
        if hun_d >=1 and hun_d <=3:
                hun_r = romanPattern['3'][1]*hun_d
        elif hun_d ==4:
            hun_r = romanPattern['3'][2]                    
        elif hun_d >=5 and hun_d <=8:
            hun_r = romanPattern['3'][3] + romanPattern['3'][1]*(hun_d - 5)
        elif hun_d == 9:
            hun_r = romanPattern['3'][4]
            print hun_r
            
        (ten_d, ten_mod) = divmod(hun_mod,10)#check the tens
        if ten_d >=1 and ten_d <=3:
            ten_r = romanPattern['2'][1]*ten_d
        elif ten_d ==4:
            ten_r = romanPattern['2'][2]
        elif ten_d >= 5 and ten_d <=8:
            ten_r = romanPattern['2'][3] + romanPattern['2'][1]*(ten_d - 5)
        elif ten_d == 9:
            ten_r = romanPattern['2'][4]
            print ten_r
            
        #check the ones
        if ten_mod >= 1 and ten_mod<=3:
            one_r = romanPattern['1']*ten_mod
        elif ten_mod ==4:
            one_r = romanPattern['1'][1]*ten_mod
        elif ten_mod >= 5 and ten_mod<=8:
            one_r = romanPattern['1'][3] + romanPattern['1'][1]*(ten_mod-5)
        elif ten_mod ==9:
            one_r = romanPattern['1'][4]
            print one_r
            
        roman_num = th_r + hun_r + ten_r + one_r
        return roman_num
                        

        
                            
