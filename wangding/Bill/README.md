````
密文：
   rphth kpajpqat kpajpqat qpcsh, kpajpqat xchixijits wdjhth pgbxth tcsdlts qpgqpgdjh wph epixtci zcdlc yjgxhsxrixdc, rpeixkt upixvjxcv vxkxcv gtijgcts, kdxrt, wdas gtcstg rxkxaxots zxcsgts zxcsgts pri prih vdds vdds yjhixrt jcstg yjsvth iwpi gjat ctvatrits zxcsgts, zxcsgts dexcxdch etixixdcts ctrthhpgn, xih gtrdgsh, gxvwih vdds apgvt yjhixrt btgrtcpgxth fjpgitgxcv jcldgiwn adcv yjhi qtrdbth egxcrxeath phhtci aplh ctrthhpgn jiitgan kpajpqat, xcid ephh diwtg, fjpgitgxcv fjpgitgxcv stpu peetpats sthxvc gjatg jh ztei rwpcvts zcdlc, tfjpa bjijpaan qtrdbth hwpaa, dqhigjrits wtps cpixkt xckphxdc deedhxcv fjpgitgxcv hpapgn hjeedgi, lwdathdbt ejqaxhw xctkxipqan igxts hipith tfjpa ztei uxgbcthh jcsxhixcvjxhwts epgpaata sthdapixdc bpn bjaixijst bpcan wxvw igpst atkn vdds udjcspixdc wxh diwtg rpaats ephh ixbth hrpgrtan httb rpeixkt hipith axvwi strapgxcv jcuxi vjpgsh iwtgtxc iwtb lwtctktg ctrthhpgn qt stetcstci fjpgitgxcv btgrxathh igxpa axqtgin iwpi gtetpitsan pagtpsn rphth lwxrw lwtgtqn xcwpqxipcih thipqaxhwts dcan axvwi, yjhi lxiwdji hlpgbh fjpgitgxcv fjpgitgxcv, gtaxcfjxhw lpcixcv vxkxcv xbeta ugxtcsh udgbtg kdxrt ujijgt ctvatrits xi prfjxthrt sthdapixdc udgb yjsxrxpgn axkth kpajpqat sthigjrixdc kpajpqat wxh xchixijit qtilttc lpgupgt jcrdbudgipqat yjhixrt qt lwxat ctl tprw jcsxhixcvjxhwts sd hjhetcsts lwdht lpvxcv qtvjc btc peetpats xckthits, jh vdktgcbtci axvwi sxhipci vxkxcv yjsxrxpgn ztei wxhidgn dgvpcxoxcv vdds ctrthhpgn edltg, udgbtg kpajpqat yjsvth qpgqpgdjh epixtci deegthhxdch fjpgitgxcv htmth bpcan, cdi ephh gtaxpcrt zcdlc axvwi, ujijgt bxaxipgn wxvw bxvgpixdc fjpgitgxcv rdcigpri, piitcs sthigjrixkt ctl, jcpaxtcpqat, deedhxcv tpi dg kdxrt qtctuxih prih wtps tmitcs iwjh fjpgitgxcv udg id rdbeatit rdcctrits tmedhts gtijgcts tcixiat thipqaxhwxcv.
````
看到密文样式后，猜测为简单替换加密，使用在线脚本https://github.com/nian-hua/cryptography/blob/master/substitution/Quadgram/hill.py
</br>对其进行解密

````
程序输出：
最好的分数:-6604.346307在第1轮
	最合适的密钥:PQRSTUVWXYZABCDEFGHIJKLMNO
````
使用该密钥对密文进行解密：http://ctf.ssleye.com/simple.html</br>
解密结果:
````
cases valuable valuable bands, valuable instituted houses armies endowed barbarous has patient known jurisdiction, captive fatiguing giving returned, voice, hold render civilized kindred kindred act acts good good justice under judges that rule neglected kindred, kindred opinions petitioned necessary, its records, rights good large justice mercenaries quartering unworthy long just becomes principles assent laws necessary utterly valuable, into pass other, quartering quartering deaf appealed design ruler us kept changed known, equal mutually becomes shall, obstructed head native invasion opposing quartering salary support, wholesome publish inevitably tried states equal kept firmness undistinguished parallel desolation may multitude manly high trade levy good foundation his other called pass times scarcely seem captive states light declaring unfit guards therein them whenever necessary be dependent quartering merciless trial liberty that repeatedly already cases which whereby inhabitants established only light, just without swarms quartering quartering, relinquish wanting giving impel friends former voice future neglected it acquiesce desolation form judiciary lives valuable destruction valuable his institute between warfare uncomfortable justice be while new each undistinguished do suspended whose waging begun men appealed invested, us government light distant giving judiciary kept history organizing good necessary power, former valuable judges barbarous patient oppressions quartering sexes manly, not pass reliance known light, future military high migration quartering contract, attend destructive new, unalienable, opposing eat or voice benefits acts head extend thus quartering for to complete connected exposed returned entitle establishing.
````
使用以下脚本解密：
````
def bill(string,password):

    password = password[5:-1]

    temp = string.split(' ')

    flag = []

    for i in range(len(password)//2):

        flag += temp[int(password[i*2:i*2+2],16)][:1]

    for i in range(len(flag)//4):

        flag[4*i+1],flag[4*i+3] = flag[4*i+3],flag[4*i+1]

    print("flag{%s}"%(''.join(flag)))

string = input("Please input string:")

password = input("please input password:")

bill(string,password)

````







