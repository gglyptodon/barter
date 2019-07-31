# barter

barter is basically just wrapping [treepoem](https://github.com/adamchainz/treepoem) for bulk barcode generation via cmd line or a csv input file.
```
usage: barter_text.py [-h]
                      [-f {auspost,azteccode,azteccodecompact,aztecrune,bc412,channelcode,codablockf,code11,code128,code16k,code2of5,code32,code39,code39ext,code49,code93,code93ext,codeone,coop2of5,daft,databarexpanded,databarexpandedcomposite,databarexpandedstacked,databarexpandedstackedcomposite,databarlimited,databarlimitedcomposite,databaromni,databaromnicomposite,databarstacked,databarstackedcomposite,databarstackedomni,databarstackedomnicomposite,databartruncated,databartruncatedcomposite,datalogic2of5,datamatrix,datamatrixrectangular,dotcode,ean13,ean13composite,ean14,ean2,ean5,ean8,ean8composite,flattermarken,gs1-128,gs1-128composite,gs1-cc,gs1datamatrix,gs1datamatrixrectangular,gs1northamericancoupon,gs1qrcode,hanxin,hibcazteccode,hibccodablockf,hibccode128,hibccode39,hibcdatamatrix,hibcdatamatrixrectangular,hibcmicropdf417,hibcpdf417,hibcqrcode,iata2of5,identcode,industrial2of5,interleaved2of5,isbn,ismn,issn,itf14,japanpost,kix,leitcode,matrix2of5,maxicode,micropdf417,microqrcode,msi,onecode,pdf417,pdf417compact,pharmacode,pharmacode2,planet,plessey,posicode,postnet,pzn,qrcode,rationalizedCodabar,raw,royalmail,sscc18,symbol,telepen,telepennumeric,ultracode,upca,upcacomposite,upce,upcecomposite}]
                      [-H HEIGHT] [-W WIDTH] [-I] [-S SIDE_TEXT]
                      [-M SIDE_TEXT_MARGIN] [-F FONT] [--fontsize FONTSIZE]
                      text outfile

positional arguments:
  text                  text for the barcode
  outfile               output file name

optional arguments:
  -h, --help            show this help message and exit
  -f {auspost,azteccode,azteccodecompact,aztecrune,bc412,channelcode,codablockf,code11,code128,code16k,code2of5,code32,code39,code39ext,code49,code93,code93ext,codeone,coop2of5,daft,databarexpanded,databarexpandedcomposite,databarexpandedstacked,databarexpandedstackedcomposite,databarlimited,databarlimitedcomposite,databaromni,databaromnicomposite,databarstacked,databarstackedcomposite,databarstackedomni,databarstackedomnicomposite,databartruncated,databartruncatedcomposite,datalogic2of5,datamatrix,datamatrixrectangular,dotcode,ean13,ean13composite,ean14,ean2,ean5,ean8,ean8composite,flattermarken,gs1-128,gs1-128composite,gs1-cc,gs1datamatrix,gs1datamatrixrectangular,gs1northamericancoupon,gs1qrcode,hanxin,hibcazteccode,hibccodablockf,hibccode128,hibccode39,hibcdatamatrix,hibcdatamatrixrectangular,hibcmicropdf417,hibcpdf417,hibcqrcode,iata2of5,identcode,industrial2of5,interleaved2of5,isbn,ismn,issn,itf14,japanpost,kix,leitcode,matrix2of5,maxicode,micropdf417,microqrcode,msi,onecode,pdf417,pdf417compact,pharmacode,pharmacode2,planet,plessey,posicode,postnet,pzn,qrcode,rationalizedCodabar,raw,royalmail,sscc18,symbol,telepen,telepennumeric,ultracode,upca,upcacomposite,upce,upcecomposite}, --format {auspost,azteccode,azteccodecompact,aztecrune,bc412,channelcode,codablockf,code11,code128,code16k,code2of5,code32,code39,code39ext,code49,code93,code93ext,codeone,coop2of5,daft,databarexpanded,databarexpandedcomposite,databarexpandedstacked,databarexpandedstackedcomposite,databarlimited,databarlimitedcomposite,databaromni,databaromnicomposite,databarstacked,databarstackedcomposite,databarstackedomni,databarstackedomnicomposite,databartruncated,databartruncatedcomposite,datalogic2of5,datamatrix,datamatrixrectangular,dotcode,ean13,ean13composite,ean14,ean2,ean5,ean8,ean8composite,flattermarken,gs1-128,gs1-128composite,gs1-cc,gs1datamatrix,gs1datamatrixrectangular,gs1northamericancoupon,gs1qrcode,hanxin,hibcazteccode,hibccodablockf,hibccode128,hibccode39,hibcdatamatrix,hibcdatamatrixrectangular,hibcmicropdf417,hibcpdf417,hibcqrcode,iata2of5,identcode,industrial2of5,interleaved2of5,isbn,ismn,issn,itf14,japanpost,kix,leitcode,matrix2of5,maxicode,micropdf417,microqrcode,msi,onecode,pdf417,pdf417compact,pharmacode,pharmacode2,planet,plessey,posicode,postnet,pzn,qrcode,rationalizedCodabar,raw,royalmail,sscc18,symbol,telepen,telepennumeric,ultracode,upca,upcacomposite,upce,upcecomposite}
                        barcode format
  -H HEIGHT, --height HEIGHT
                        height in mm
  -W WIDTH, --width WIDTH
                        width in mm
  -I, --include_text    add human-readable text under barcode
  -S SIDE_TEXT, --side_text SIDE_TEXT
                        text to put next to barcode
  -M SIDE_TEXT_MARGIN, --side_text_margin SIDE_TEXT_MARGIN
                        spacing between barcode and text on the side (in px)
  -F FONT, --font FONT  font
  --fontsize FONTSIZE   font size
```


```
usage: barter_csv.py [-h]
                     [-f {auspost,azteccode,azteccodecompact,aztecrune,bc412,channelcode,codablockf,code11,code128,code16k,code2of5,code32,code39,code39ext,code49,code93,code93ext,codeone,coop2of5,daft,databarexpanded,databarexpandedcomposite,databarexpandedstacked,databarexpandedstackedcomposite,databarlimited,databarlimitedcomposite,databaromni,databaromnicomposite,databarstacked,databarstackedcomposite,databarstackedomni,databarstackedomnicomposite,databartruncated,databartruncatedcomposite,datalogic2of5,datamatrix,datamatrixrectangular,dotcode,ean13,ean13composite,ean14,ean2,ean5,ean8,ean8composite,flattermarken,gs1-128,gs1-128composite,gs1-cc,gs1datamatrix,gs1datamatrixrectangular,gs1northamericancoupon,gs1qrcode,hanxin,hibcazteccode,hibccodablockf,hibccode128,hibccode39,hibcdatamatrix,hibcdatamatrixrectangular,hibcmicropdf417,hibcpdf417,hibcqrcode,iata2of5,identcode,industrial2of5,interleaved2of5,isbn,ismn,issn,itf14,japanpost,kix,leitcode,matrix2of5,maxicode,micropdf417,microqrcode,msi,onecode,pdf417,pdf417compact,pharmacode,pharmacode2,planet,plessey,posicode,postnet,pzn,qrcode,rationalizedCodabar,raw,royalmail,sscc18,symbol,telepen,telepennumeric,ultracode,upca,upcacomposite,upce,upcecomposite}]
                     [-c COLUMN] [-H HEIGHT] [-W WIDTH] [-I]
                     [-S SIDE_TEXT_COLUMN] [-M SIDE_TEXT_MARGIN] [-F FONT]
                     [--fontsize FONTSIZE]
                     infile outdir

positional arguments:
  infile                input csv file
  outdir                output directory name

optional arguments:
  -h, --help            show this help message and exit
  -f {auspost,azteccode,azteccodecompact,aztecrune,bc412,channelcode,codablockf,code11,code128,code16k,code2of5,code32,code39,code39ext,code49,code93,code93ext,codeone,coop2of5,daft,databarexpanded,databarexpandedcomposite,databarexpandedstacked,databarexpandedstackedcomposite,databarlimited,databarlimitedcomposite,databaromni,databaromnicomposite,databarstacked,databarstackedcomposite,databarstackedomni,databarstackedomnicomposite,databartruncated,databartruncatedcomposite,datalogic2of5,datamatrix,datamatrixrectangular,dotcode,ean13,ean13composite,ean14,ean2,ean5,ean8,ean8composite,flattermarken,gs1-128,gs1-128composite,gs1-cc,gs1datamatrix,gs1datamatrixrectangular,gs1northamericancoupon,gs1qrcode,hanxin,hibcazteccode,hibccodablockf,hibccode128,hibccode39,hibcdatamatrix,hibcdatamatrixrectangular,hibcmicropdf417,hibcpdf417,hibcqrcode,iata2of5,identcode,industrial2of5,interleaved2of5,isbn,ismn,issn,itf14,japanpost,kix,leitcode,matrix2of5,maxicode,micropdf417,microqrcode,msi,onecode,pdf417,pdf417compact,pharmacode,pharmacode2,planet,plessey,posicode,postnet,pzn,qrcode,rationalizedCodabar,raw,royalmail,sscc18,symbol,telepen,telepennumeric,ultracode,upca,upcacomposite,upce,upcecomposite}, --format {auspost,azteccode,azteccodecompact,aztecrune,bc412,channelcode,codablockf,code11,code128,code16k,code2of5,code32,code39,code39ext,code49,code93,code93ext,codeone,coop2of5,daft,databarexpanded,databarexpandedcomposite,databarexpandedstacked,databarexpandedstackedcomposite,databarlimited,databarlimitedcomposite,databaromni,databaromnicomposite,databarstacked,databarstackedcomposite,databarstackedomni,databarstackedomnicomposite,databartruncated,databartruncatedcomposite,datalogic2of5,datamatrix,datamatrixrectangular,dotcode,ean13,ean13composite,ean14,ean2,ean5,ean8,ean8composite,flattermarken,gs1-128,gs1-128composite,gs1-cc,gs1datamatrix,gs1datamatrixrectangular,gs1northamericancoupon,gs1qrcode,hanxin,hibcazteccode,hibccodablockf,hibccode128,hibccode39,hibcdatamatrix,hibcdatamatrixrectangular,hibcmicropdf417,hibcpdf417,hibcqrcode,iata2of5,identcode,industrial2of5,interleaved2of5,isbn,ismn,issn,itf14,japanpost,kix,leitcode,matrix2of5,maxicode,micropdf417,microqrcode,msi,onecode,pdf417,pdf417compact,pharmacode,pharmacode2,planet,plessey,posicode,postnet,pzn,qrcode,rationalizedCodabar,raw,royalmail,sscc18,symbol,telepen,telepennumeric,ultracode,upca,upcacomposite,upce,upcecomposite}
                        barcode format
  -c COLUMN, --column COLUMN
                        column for which labels should be generated
  -H HEIGHT, --height HEIGHT
                        height in mm
  -W WIDTH, --width WIDTH
                        width in mm
  -I, --include_text    add human-readable text
  -S SIDE_TEXT_COLUMN, --side_text_column SIDE_TEXT_COLUMN
                        column for additional text
  -M SIDE_TEXT_MARGIN, --side_text_margin SIDE_TEXT_MARGIN
                        spacing between barcode and text on the side (in px)
  -F FONT, --font FONT  font
  --fontsize FONTSIZE   font size
```

## Example output

```
barter_text.py "https://github.com/gglyptodon/barter" ~/Desktop/barter_url.png  -W 30 -H 30 -F Ubuntu-R.ttf --fontsize 30  -f qrcode -S https://github.com/gglyptodon/barter -M0
```
![](https://raw.githubusercontent.com/gglyptodon/barter/master/barter/example/pics/url.png)


```
barter_text.py https://github.com/gglyptodon/barter  ~/Desktop/url_barcode.png  -W 30 -H 30 -f qrcode
```
![](https://raw.githubusercontent.com/gglyptodon/barter/master/barter/example/pics/url_barcode.png)
