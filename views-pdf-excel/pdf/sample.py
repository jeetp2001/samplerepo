import psycopg2
import webbrowser
import pdfkit

con = psycopg2.connect(host='localhost',user='postgres',password='jeetp2001',database='gst')
cur = con.cursor()

q1 = 'select * from txnvalidations'
cur.execute(q1)
data1 = cur.fetchall()

q2='select * from gstr1b2c'
cur.execute(q2)
data2 = cur.fetchall()

q3 = 'select * from gst1hsn'
cur.execute(q3)
data3 = cur.fetchall()

q4='select * from gstr3b'
cur.execute(q4)
data4 = cur.fetchall()

q5='select * from dumperrors order by errorlevel,column_name'
cur.execute(q5)
data5 = cur.fetchall()

q6='select * from mastererrorview order by errorlevel'
cur.execute(q6)
data6=cur.fetchall()


tbl1 = "<tr><th>CSV RowNumber</th><th>Invoice Number</th><th>Booth Name And Number</th><th>Error Message</th><th>Error Name</th><th>Period</th><th>Customer GSTIN</th><th>Error Level</th></tr>"
l1=[]
l1.append(tbl1)

tbl2 = "<tr><th>Return Period</th><th>GSTIN</th><th>GST</th><th>Quantity</th><th>Total</th><th>Taxable Value</th><th>CGST</th><th>SGST</th></tr>"
l2=[]
l2.append(tbl2)


tbl3 = "<tr><th>Return Period</th><th>HSN</th><th>GSTIN</th><th>Unit Of Measurement</th><th>GST</th><th>Quantity</th><th>Total</th><th>Taxable Value</th><th>CGST</th><th>SGST</th></tr>"
l3 = []
l3.append(tbl3)

tbl4 = "<tr><th>Return Period</th><th>GSTIN</th><th>Total Sale Invoice Value</th><th>Taxable Sale Value</th><th>Sale CGST</th><th>Sale SGST</th><th>Exempt Sale Invoice Value</th><th>Exempt Purchase Value Intra</th><th>Exempt Purchase Value Inter</th><th>Taxable Purchase Value</th><th>PurIntegrated Tax Amount</th><th>PurCentral Tax Amount</th><th>PurStateUT Tax Amount</th><th>PurCess Amount Advalorem</th><th>PurCess Amount Specific</th><th>CGST Payable</th><th>SGST Payable</th></tr>"
l4 = []
l4.append(tbl4)

tbl5 = "<tr><th>Error Level</th><th>Error Reason</th><th>Error Type</th><th>Column Name</th><th>Value Expected</th><th>Value in CSV</th><th>Number of Instances</th></tr>"
l5=[]
l5.append(tbl5)


tbl6 = "<tr><th>Error Level</th><th>Error Reason</th><th>Error Type</th><th>Column Name</th><th>Number of Instances</th></tr>"
l6=[]
l6.append(tbl6)


for i in data1:
    if str(i[0]).replace('.','',1).isdigit():
        a="<tr><td align=right>%s</td>"%i[0]
    else:
        a="<tr><td align=left>%s</td>"%i[0]    
    l1.append(a)
    if str(i[1]).replace('.','',1).isdigit():
        b="<td align=right>%s</td>"%i[1]
    else:
        b="<td align=left>%s</td>"%i[1]
    l1.append(b)
    if str(i[2]).replace('.','',1).isdigit():
        c="<td align=right>%s</td>"%i[2]
    else:
        c="<td align=left>%s</td>"%i[2]
    l1.append(c)
    if str(i[3]).replace('.','',1).isdigit():
        d="<td align=right>%s</td>"%i[3]
    else:
        d="<td align=left>%s</td>"%i[3]
    l1.append(d)
    if str(i[4]).replace('.','',1).isdigit():
        e="<td align=right>%s</td>"%i[4]
    else:
        e="<td align=left>%s</td>"%i[4]
    l1.append(e)
    if str(i[5]).replace('.','',1).isdigit():
        f="<td align=right>%s</td>"%i[5]
    else:
        f="<td align=left>%s</td>"%i[5]
    l1.append(f)
    if str(i[6]).replace('.','',1).isdigit():
        g="<td align=right>%s</td>"%i[6]
    else:
        g="<td align=left>%s</td>"%i[6]
    l1.append(g)
    if str(i[7]).replace('.','',1).isdigit():
        h="<td align=right>%s</td></tr>"%i[7]
    else:
        h="<td align=left>%s</td></tr>"%i[7]
    l1.append(h)


for i  in data2:
    if str(i[0]).replace('.','',1).isdigit():
        n1='<tr><td align=right>%s</td>'%i[0]
    else:
        n1='<tr><td align=left>%s</td>'%i[0]
    l2.append(n1)
    if str(i[1]).replace('.','',1).isdigit():
        n2='<td align=right>%s</td>'%i[1]
    else:
        n2='<td align=left>%s</td>'%i[1]
    l2.append(n2)
    if str(i[2]).replace('.','',1).isdigit():
        n3='<td align=right>%s</td>'%i[2]
    else:
        n3='<td align=left>%s</td>'%i[2]
    l2.append(n3)
    if str(i[3]).replace('.','',1).isdigit():
        n4='<td align=right>%s</td>'%i[3]
    else:
        n4='<td align=left>%s</td>'%i[3]
    l2.append(n4)
    if str(i[4]).replace('.','',1).isdigit():
        n5='<td align=right>%s</td>'%i[4]
    else:
        n5='<td align=left>%s</td>'%i[4]
    l2.append(n5)
    if str(i[5]).replace('.','',1).isdigit():
        n6='<td align=right>%s</td>'%i[5]
    else:
        n6='<td align=left>%s</td>'%i[5]
    l2.append(n6)
    if str(i[6]).replace('.','',1).isdigit():
        n7='<td align=right>%s</td>'%i[6]
    else:
        n7='<td align=left>%s</td>'%i[6]
    l2.append(n7)
    if str(i[7]).replace('.','',1).isdigit():
        n8='<td align=right>%s</td></tr>'%i[7]
    else:
        n8='<td align=left>%s</td></tr>'%i[7]
    l2.append(n8)
    
for i in data3:
    if str(i[0]).replace('.','',1).isdigit():
        n1='<tr><td align=right>%s</td>'%i[0]
    else:
        n1='<tr><td align=left>%s</td>'%i[0]
    l3.append(n1)
    if str(i[1]).replace('.','',1).isdigit():
        n2='<td align=right>%s</td>'%i[1]
    else:
        n2='<td align=left>%s</td>'%i[1]
    l3.append(n2)
    if str(i[2]).replace('.','',1).isdigit():
        n3='<td align=right>%s</td>'%i[2]
    else:
        n3='<td align=left>%s</td>'%i[2]
    l3.append(n3)
    if str(i[3]).replace('.','',1).isdigit():
        n4='<td align=right>%s</td>'%i[3]
    else:
        n4='<td align=left>%s</td>'%i[3]
    l3.append(n4)
    if str(i[4]).replace('.','',1).isdigit():
        n5='<td align=right>%s</td>'%i[4]
    else:
        n5='<td align=left>%s</td>'%i[4]
    l3.append(n5)
    if str(i[5]).replace('.','',1).isdigit():
        n6='<td align=right>%s</td>'%i[5]
    else:
        n6='<td align=left>%s</td>'%i[5]
    l3.append(n6)
    if str(i[6]).replace('.','',1).isdigit():
        n7='<td align=right>%s</td>'%i[6]
    else:
        n7='<td align=left>%s</td>'%i[6]
    l3.append(n7)
    if str(i[7]).replace('.','',1).isdigit():
        n8='<td align=right>%s</td>'%i[7]
    else:
        n8='<td align=left>%s</td>'%i[7]
    l3.append(n8)
    if str(i[8]).replace('.','',1).isdigit():
        n9='<td align=right>%s</td>'%i[8]
    else:
        n9='<td align=left>%s</td>'%i[8]
    l3.append(n9)
    if str(i[9]).replace('.','',1).isdigit():
        n10='<td align=right>%s</td></tr>'%i[9]
    else:
        n10='<td align=left>%s</td></tr>'%i[9]
    l3.append(n10)    
    
for i in data4:
    if str(i[0]).replace('.','',1).isdigit():
        n1='<tr><td align=right>%s</td>'%i[0]
    else:
        n1='<tr><td align=left>%s</td>'%i[0]
    l4.append(n1)
    if str(i[1]).replace('.','',1).isdigit():
        n2='<td align=right>%s</td>'%i[1]
    else:
        n2='<td align=left>%s</td>'%i[1]
    l4.append(n2)
    if str(i[2]).replace('.','',1).isdigit():
        n3='<td align=right>%s</td>'%i[2]
    else:
        n3='<td align=left>%s</td>'%i[2]
    l4.append(n3)
    if str(i[3]).replace('.','',1).isdigit():
        n4='<td align=right>%s</td>'%i[3]
    else:
        n4='<td align=left>%s</td>'%i[3]
    l4.append(n4)
    if str(i[4]).replace('.','',1).isdigit():
        n5='<td align=right>%s</td>'%i[4]
    else:
        n5='<td align=left>%s</td>'%i[4]
    l4.append(n5)
    if str(i[5]).replace('.','',1).isdigit():
        n6='<td align=right>%s</td>'%i[5]
    else:
        n6='<td align=left>%s</td>'%i[5]
    l4.append(n6)
    if str(i[6]).replace('.','',1).isdigit():
        n7='<td align=right>%s</td>'%i[6]
    else:
        n7='<td align=left>%s</td>'%i[6]
    l4.append(n7)
    if str(i[7]).replace('.','',1).isdigit():
        n8='<td align=right>%s</td>'%i[7]
    else:
        n8='<td align=left>%s</td>'%i[7]
    l4.append(n8)
    if str(i[8]).replace('.','',1).isdigit():
        n9='<td align=right>%s</td>'%i[8]
    else:
        n9='<td align=left>%s</td>'%i[8]
    l4.append(n9)
    if str(i[9]).replace('.','',1).isdigit():
        n10='<td align=right>%s</td>'%i[9]
    else:
        n10='<td align=left>%s</td>'%i[9]
    l4.append(n10)    
    if str(i[10]).replace('.','',1).isdigit():
        n11='<td align=right>%s</td>'%i[10]
    else:
        n11='<td align=left>%s</td>'%i[10]
    l4.append(n11)
    if str(i[11]).replace('.','',1).isdigit():
        n12='<td align=right>%s</td>'%i[11]
    else:
        n12='<td align=left>%s</td>'%i[11]
    l4.append(n12)
    if str(i[12]).replace('.','',1).isdigit():
        n13='<td align=right>%s</td>'%i[12]
    else:
        n13='<td align=left>%s</td>'%i[12]
    l4.append(n13)
    if str(i[13]).replace('.','',1).isdigit():
        n14='<td align=right>%s</td>'%i[13]
    else:
        n14='<td align=left>%s</td>'%i[13]
    l4.append(n14)
    if str(i[14]).replace('.','',1).isdigit():
        n15='<td align=right>%s</td>'%i[14]
    else:
        n15='<td align=left>%s</td>'%i[14]
    l4.append(n15)
    if str(i[15]).replace('.','',1).isdigit():
        n16='<td align=right>%s</td>'%i[15]
    else:
        n16='<td align=left>%s</td>'%i[15]
    l4.append(n16)
    if str(i[16]).replace('.','',1).isdigit():
        n17='<td align=right>%s</td></tr>'%i[16]
    else:
        n17='<td align=left>%s</td></tr>'%i[16]
    l4.append(n17)

for i  in data5:
    if str(i[0]).replace('.','',1).isdigit():
        n1='<tr><td align=right>%s</td>'%i[0]
    else:
        n1='<tr><td align=left>%s</td>'%i[0]
    l5.append(n1)
    if str(i[1]).replace('.','',1).isdigit():
        n2='<td align=right>%s</td>'%i[1]
    else:
        n2='<td align=left>%s</td>'%i[1]
    l5.append(n2)
    if str(i[2]).replace('.','',1).isdigit():
        n3='<td align=right>%s</td>'%i[2]
    else:
        n3='<td align=left>%s</td>'%i[2]
    l5.append(n3)
    if str(i[3]).replace('.','',1).isdigit():
        n4='<td align=right>%s</td>'%i[3]
    else:
        n4='<td align=left>%s</td>'%i[3]
    l5.append(n4)
    if str(i[4]).replace('.','',1).isdigit():
        n5='<td align=right>%s</td>'%i[4]
    else:
        n5='<td align=left>%s</td>'%i[4]
    l5.append(n5)
    if str(i[5]).replace('.','',1).isdigit():
        n6='<td align=right>%s</td>'%i[5]
    else:
        n6='<td align=left>%s</td>'%i[5]
    l5.append(n6)
    if str(i[6]).replace('.','',1).isdigit():
        n7='<td align=right>%s</td>'%i[6]
    else:
        n7='<td align=left>%s</td>'%i[6]
    l5.append(n7)
    
for i  in data6:
    if str(i[0]).replace('.','',1).isdigit():
        n1='<tr><td align=right>%s</td>'%i[0]
    else:
        n1='<tr><td align=left>%s</td>'%i[0]
    l6.append(n1)
    if str(i[1]).replace('.','',1).isdigit():
        n2='<td align=right>%s</td>'%i[1]
    else:
        n2='<td align=left>%s</td>'%i[1]
    l6.append(n2)
    if str(i[2]).replace('.','',1).isdigit():
        n3='<td align=right>%s</td>'%i[2]
    else:
        n3='<td align=left>%s</td>'%i[2]
    l6.append(n3)
    if str(i[3]).replace('.','',1).isdigit():
        n4='<td align=right>%s</td>'%i[3]
    else:
        n4='<td align=left>%s</td>'%i[3]
    l6.append(n4)
    if str(i[4]).replace('.','',1).isdigit():
        n5='<td align=right>%s</td>'%i[4]
    else:
        n5='<td align=left>%s</td>'%i[4]
    l6.append(n5)
   

str1 = ''.join([str(i) for i in l1])
str2 = ''.join([str(i) for i in l2])
str3 = ''.join([str(i) for i in l3])
str4 = ''.join([str(i) for i in l4])
str5 = ''.join([str(i) for i in l5])
str6 = ''.join([str(i) for i in l6])


contents1 = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="pdfkit-orientation" content="Landscape"/>
    <title>Document</title>
    <link rel='stylesheet' href='css.css'>
    <style>
        th,td {
            padding: 15px;
        }
    </style>
</head>
<body>
    <div align=center><u><h1>Transaction Errors</h1></u></div>
    <table class='t1' align=center>
        %s
    </table>
</body>
</html>
'''%str1


contents2 = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="pdfkit-orientation" content="Landscape"/>
    <title>Document</title>
    <link rel='stylesheet' href='css.css'>
    <style>
        th,td {
            padding: 15px;
        }
    </style>
</head>
<body>
    <div align=center><u><h1>GSTR-1B2C</h1></u></div>
    <table class='t2' align=center>
        %s
    </table>
</body>
</html>
'''%str2


contents3 = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="pdfkit-orientation" content="Landscape"/>
    <title>Document</title>
    <link rel='stylesheet' href='css.css'>
    <style>
        th,td {
            padding: 15px;
        }
    </style>
</head>
<body>
    <div align=center><u><h1>GST-1HSN</h1></u></div>
    <table class='t3' align=center>
        %s
    </table>
</body>
</html>
'''%str3

contents4 = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="pdfkit-orientation" content="Landscape"/>
    <title>Document</title>
    <link rel='stylesheet' href='css.css'>
    <style>
        th,td {
            padding: 20px;
        }
    </style>
</head>
<body>
    <div align=center><u><h1>GSTR-3B</h1></u></div>
    <table class='t4' align=center>
        %s
    </table>
</body>
</html>
'''%str4

contents5 = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="pdfkit-orientation" content="Landscape"/>
    <title>Document</title>
    <link rel='stylesheet' href='css.css'>
    <style>
        th,td {
            padding: 15px;
        }
    </style>
</head>
<body>
    <div align=center><u><h1>Dump Errors</h1></u></div>
    <table class='t2' align=center>
        %s
    </table>
</body>
</html>
'''%str5

contents6 = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="pdfkit-orientation" content="Landscape"/>
    <title>Document</title>
    <link rel='stylesheet' href='css.css'>
    <style>
        th,td {
            padding: 15px;
        }
    </style>
</head>
<body>
    <div align=center><u><h1>Error Summary</h1></u></div>
    <table class='t2' align=center>
        %s
    </table>
</body>
</html>
'''%str6

filename1 = 'Transaction Errors.html'
filename2 = 'GSTR-1B2C.html'
filename3 = 'GSTR-1HSN.html'
filename4 = 'GSTR-3B.html'
filename5 = 'Dump Errors.html'
filename6 = 'Error Summary.html'

def main(contents,filename):
    output = open(filename,"w")
    output.write(contents)
    output.close()

main(contents1,filename1)
main(contents2,filename2)
main(contents3,filename3)
main(contents4,filename4)
main(contents5,filename5)
main(contents6,filename6)


options4 = {
    'page-size': 'A4',
    'margin-top': '5',
    'margin-right': '5',
    'margin-bottom': '20',
    'margin-left': '10',
    'encoding': "UTF-8",
    'page-width': '7in',
    'page-height': '24in',
    'orientation': "Landscape"
}


pdfkit.from_file([filename6,filename1,filename2,filename3,filename4],'GSTR Filing Data - 092021.pdf',options=options4)

print('done...')
