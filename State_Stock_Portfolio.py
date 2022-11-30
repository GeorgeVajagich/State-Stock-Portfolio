import yfinance as yf
import matplotlib.pyplot as plt

#SP500 tickers as of 11/6/2022
SP500=["AAPL","MSFT","AMZN","TSLA","BRK.B","UNH","GOOGL","XOM","JNJ","JPM","NVDA","CVX","V","PG","HD","LLY","MA","PFE","ABBV","BAC","MRK","PEP","KO","COST","META","MCD","WMT","TMO","CSCO","DIS","AVGO","WFC","COP","ABT","BMY","ACN","DHR","VZ","NEE","LIN","CRM","TXN","AMGN","RTX","HON","PM","ADBE","CMCSA","T","CVS","ELV","IBM","UNP","SCHW","UPS","NFLX","GS","QCOM","CAT","LOW","LMT","NKE","ORCL","INTC","MS","MDT","DE","SPGI","INTU","GILD","PLD","CI","ADP","AMD","SBUX","BLK","AMT","TMUS","PYPL","CB","BA","C","GE","MDLZ","AXP","ISRG","TJX","EOG","MO","VRTX","MMC","REGN","NOW","NOC","AMAT","PGR","TGT","SLB","BKNG","ADI","DUK","HUM","SYK","SO","MMM","BDX","PNC","CSX","ETN","ZTS","CME","PXD","FISV","CL","ITW","BSX","WM","MU","MPC","APD","AON","D","MCK","DG","TFC","USB","GM","GD","CCI","ADM","LRCX","OXY","NSC","ICE","EQIX","F","ORLY","EMR","SHW","ATVI","VLO","MRNA","PSX","MET","CNC","AZO","CTVA","SRE","GIS","DVN","HCA","AEP","FCX","LHX","EL","KLAC","DXCM","APH","AIG","PSA","TRV","SNPS","EW","ADSK","ROP","JCI","SYY","KMB","BIIB","WMB","MCO","MAR","A","ENPH","MSI","AJG","HES","CDNS","CMG","STZ","TT","CHTR","O","IQV","NXPI","AFL","COF","PRU","FDX","SPG","EXC","PH","MSCI","TEL","PAYX","KMI","XEL","CTAS","HLT","MNST","FIS","HSY","YUM","NUE","ALL","EA","DOW","PCAR","AMP","CARR","HAL","DLTR","ILMN","CMI","MCHP","ECL","ROST","ALB","CSGP","ED","KR","KDP","IDXX","VICI","BK","CEG","RMD","KHC","AME","ANET","FTNT","KEYS","NEM","DD","OTIS","SBAC","TDG","MTB","BKR","PEG","WEC","FANG","ROK","MTD","FAST","DLR","RSG","WELL","GWW","CTSH","DFS","STT","ES","WBD","OKE","GPN","VRSK","PPG","ON","WBA","BAX","IT","GPC","AWK","APTV","ABC","CTRA","HPQ","GLW","PCG","ODFL","CPRT","WTW","IFF","AVB","HIG","TSCO","DHI","CDW","FITB","RJF","TROW","VMC","ETR","FTV","URI","CBRE","EIX","WY","ZBH","LUV","ULTA","DTE","HBAN","EBAY","MRO","ARE","CF","NDAQ","FE","EQR","AEE","RF","FRC","CAH","IR","ACGL","MOH","MLM","PWR","EXR","DAL","LH","LEN","PFG","LYB","PPL","TSN","EFX","CFG","XYL","MKC","DOV","HOLX","ANSS","INVH","TDY","WAT","HPE","K","CNP","TTWO","MAA","CHD","AES","EPAM","DRI","CAG","NTRS","WAB","MOS","CLX","VRSN","ABMD","DGX","IEX","KEY","SYF","CMS","AMCR","STE","BALL","PKI","SJM","TRGP","PAYC","FMC","EXPD","FDS","CINF","APA","BR","WST","WRB","NTAP","MPWR","J","VTR","OMC","LDOS","ATO","EQT","IRM","INCY","TXT","JBHT","EVRG","ESS","AVY","BBY","LKQ","HRL","AKAM","SWKS","CBOE","JKHY","BRO","EXPE","RE","FLT","UAL","HWM","TRMB","GRMN","COO","LNT","PTC","PEAK","ALGN","KIM","DPZ","ETSY","TER","NVR","NLOK","LVS","SEDG","LW","SIVB","MTCH","BF.B","HST","TYL","IP","SNA","RCL","ZBRA","TECH","NDSN","CPT","VTRS","POOL","UDR","PKG","IPG","AAP","CHRW","LYV","CRL","L","SWK","WDC","NI","CPB","NRG","MGM","KMX","GL","BXP","HSIC","HII","CDAY","MAS","JNPR","STX","CE","ROL","EMN","TFX","TAP","FOXA","CZR","REG","ALLE","SBNY","AAL","VFC","CMA","BWA","MKTX","PHM","CCL","QRVO","WRK","PARA","FFIV","RHI","HAS","BIO","PNW","TPR","CTLT","BBWI","UHS","ZION","FBHS","NCLH","WHR","AOS","WYNN","FRT","IVZ","PNR","AIZ","OGN","NWSA","GNRC","SEE","BEN","DXC","XRAY","ALK","LNC","LUMN","NWL","MHK","FOX","RL","DVA","VNO","DISH","NWS"]

States=[]


Choice=input("Which states' companies would you like to be in your portfolio (type an abbreviation like TX or NY)")
print("Now wait a while; this could take up to 20 minutes")

for s in range(0,502):
    P = round(0.2 * s,1)
    P=str(P)
    print(P + "%", end='\r')
    tick = yf.Ticker(SP500[s])
    try:
        States.append(tick.info["state"])
    except:
        States.append("null")


stocksInState=[]
for i in range (0,502):
    P = round(0.2 * i,1)
    P=str(P)
    print(P + "%", end='\r')
    if States[i]==Choice:
        stocksInState.append((SP500[i]))

Caps=[]
Names=[]

for s in stocksInState:
    s = yf.Ticker(s)
    Caps.append(s.info["marketCap"])
    Names.append(s.info["shortName"])

# calculate and print what percentage of the portfolio each constituent company is
for i in range(0,len(Names)):
    percent=(Caps[i])/sum(Caps)*100
    percent=str(percent)
    print(Names[i]+" "+percent+"%")

# creates a pie chart showing the distribution of stocks in this state portfolio
plt.pie(Caps,labels=Names)
plt.savefig(Choice + " portfolio.png")