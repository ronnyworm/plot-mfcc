Mit diesem Skript werden die Samples von speech01.wav geplottet (50-fach verstärkt).
Dazu aber auch die MFCCs (inkl. delta und deltadelta) (ohne Verstärkung).

## MFCCs
Die MFCCs in outmfcc_D_A.csv wurden vorher mit diesem Kommando extrahiert:

    time SMILExtract -C config/MFCC12_0_D_A.conf -I speech01.wav -csvoutput outmfcc_D_A.csv

Die config-Datei ist bei OpenSMILE dabei.

## Samples
Die Samples wurden mit sox so extrahiert:

    sox speech01.wav -t dat out.txt
    # csv-like
    # sed -E wegen Mac OS
    cat out.txt | sed -E -e 's/^ +//g' -e 's/  +/;/g' > samples.csv

## Ergebnis
![asdf](result.png)