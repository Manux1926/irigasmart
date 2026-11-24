from build import AFF_NOTE

JS = r"""
(function(){
function $(s){return document.querySelector(s)}
function f(x,d){return (+x).toLocaleString('ro-RO',{maximumFractionDigits:d||0})}
var c=$('#calc');if(c){
 function run(){var t=$('#tip').value,a=+$('#arie').value||0,lu=+$('#luna').value,pl=+$('#ploaie').value||0,ud=+$('#ud').value||1,pr=+$('#pret').value||0,sys=$('#sys').value;
  var mm={gazon:30,legume:28,flori:20,pomi:0}[t];
  var need=t==='pomi'?a*45*lu:Math.max(0,(mm*lu-pl*0.8))*a;
  if(t==='pomi')need=Math.max(0,need-pl*0.8*a*4);
  var perUd=need/ud;var min=0,note='';
  if(sys==='picurare'){var sp=t==='pomi'?0:0.3*0.4;var n=t==='pomi'?a*4:Math.ceil(a/sp);var q=+$('#deb').value||2;min=n>0?perUd/(n*q)*60:0;note=f(n)+' picurători de '+q+' L/h'}
  else{var rate=sys==='rotor'?12:35;min=a>0&&t!=='pomi'?(perUd/a)/rate*60:0;note='rată de aplicare ~'+rate+' mm/oră'}
  var luna=need*4.3/1000*pr;
  $('#rL').textContent=f(need)+' L/săpt.';$('#rMin').textContent=f(min)+' min';$('#rNote').textContent=note;$('#rCost').textContent=f(luna)+' lei/lună';$('#rM3').textContent=f(need*4.3/1000,1)+' m³/lună';}
 c.addEventListener('input',run);c.addEventListener('change',run);run();}
var r=$('#rain');if(r){function rr(){var s=+$('#acop').value||0,p=+$('#pp').value||0;var l=s*p*0.85;$('#rr').textContent=f(l)+' litri';$('#rb').textContent=f(Math.ceil(l/300))+' butoaie de 300 L'}r.addEventListener('input',rr);rr()}
})();
"""

TOOL = """<div class="tool"><form id="calc" onsubmit="return false"><h2>Calculator irigații: câtă apă și câte minute</h2>
<div class="grid3">
<div><label class="f" for="tip">Ce uzi</label><select id="tip"><option value="gazon">Gazon</option><option value="legume" selected>Grădină de legume</option><option value="flori">Flori și arbuști</option><option value="pomi">Pomi fructiferi (număr de pomi)</option></select></div>
<div><label class="f" for="arie">Suprafață (m²) sau număr de pomi</label><input id="arie" type="number" min="0" value="60"></div>
<div><label class="f" for="luna">Luna</label><select id="luna"><option value="0.5">Aprilie</option><option value="0.7">Mai</option><option value="0.9">Iunie</option><option value="1" selected>Iulie</option><option value="1">August</option><option value="0.6">Septembrie</option></select></div>
<div><label class="f" for="ploaie">Ploaie în ultima săptămână (mm)</label><input id="ploaie" type="number" min="0" value="0"></div>
<div><label class="f" for="ud">Udări pe săptămână</label><input id="ud" type="number" min="1" max="14" value="3"></div>
<div><label class="f" for="sys">Sistem</label><select id="sys"><option value="picurare">Picurare</option><option value="rotor">Aspersoare rotative</option><option value="spray">Aspersoare fixe (spray)</option></select></div>
<div><label class="f" for="deb">Debit picurător (L/h)</label><select id="deb"><option>2</option><option>4</option><option>8</option></select></div>
<div><label class="f" for="pret">Prețul apei (lei/m³)</label><input id="pret" type="number" min="0" step="0.1" value="8"></div>
</div>
<div class="res"><div class="big"><div class="kpi"><span>Necesar de apă</span><b id="rL">–</b></div><div class="kpi main"><span>Durată pe udare</span><b id="rMin">–</b></div><div class="kpi"><span>Consum</span><b id="rM3">–</b></div><div class="kpi"><span>Cost apă</span><b id="rCost">–</b></div></div>
<p class="note" style="margin-top:8px">Calculat pentru: <b id="rNote"></b>. Picurători la 30 cm pe rând, rânduri la 40 cm; la pomi, 4 picurători pe pom. Valorile sunt orientative: solul nisipos cere udări mai dese și mai scurte, cel argilos invers.</p></div></form></div>"""

RAIN = """<div class="tool" style="margin-top:24px"><form id="rain" onsubmit="return false"><h2>Câtă apă de ploaie poți colecta?</h2>
<div class="grid2"><div><label class="f" for="acop">Suprafața acoperișului (m², proiecție orizontală)</label><input id="acop" type="number" min="0" value="100"></div>
<div><label class="f" for="pp">Ploaie (mm) – o ploaie de vară obișnuită: 10–20 mm</label><input id="pp" type="number" min="0" value="15"></div></div>
<div class="res"><div class="big"><div class="kpi main"><span>Apă colectată</span><b id="rr">–</b></div><div class="kpi"><span>Ai nevoie de</span><b id="rb">–</b></div></div><p class="note">1 mm de ploaie pe 1 m² înseamnă 1 litru. Socotim pierderi de 15%.</p></div></form></div>"""

INDEX_BODY = TOOL + """
<section class="sec"><h2>De ce irigarea prin picurare câștigă teren</h2>
<p>Verile tot mai secetoase din România fac din udatul grădinii o problemă de timp și de bani. Picurarea duce apa direct la rădăcină, cu pierderi mici prin evaporare, și se poate automatiza complet cu un programator de robinet. Aspersoarele rămân cea mai bună soluție pentru gazon.</p>
<ul><li><strong>Udă rar și profund</strong>, nu puțin și des: rădăcinile coboară și plantele rezistă mai bine la caniculă.</li><li><strong>Udă dimineața devreme:</strong> pierzi mai puțină apă prin evaporare și reduci bolile frunzelor.</li><li><strong>Un pluviometru ieftin</strong> îți spune exact câtă ploaie a căzut, ca să scazi din udare.</li></ul></section>
""" + RAIN + """
<section class="sec"><h2>Ghiduri</h2><div class="cards">
<a class="c" href="/picurare-sau-aspersoare.html"><span class="tag">Comparație</span><b>Picurare sau aspersoare?</b><span>Ce alegi pentru legume, gazon și pomi.</span></a>
<a class="c" href="/sistem-irigatii-gradina-legume.html"><span class="tag">Pas cu pas</span><b>Sistem de picurare pentru legume</b><span>Ce cumperi și cum îl montezi într-o zi.</span></a>
<a class="c" href="/programator-irigatii.html"><span class="tag">Smart</span><b>Programatoare de irigații</b><span>De robinet, cu Wi-Fi, cu senzor de ploaie.</span></a></div></section>"""

FAQ = [
    ('Câtă apă îi trebuie gazonului vara?', 'În zilele călduroase din iulie și august, în jur de 25–35 mm pe săptămână, adică 25–35 de litri pe metru pătrat, din ploaie și udare la un loc. Împarte-i în 2–3 udări profunde.'),
    ('Cât timp las picurarea pornită?', 'Depinde de debitul picurătorilor și de distanța dintre ei. Ca reper, cu picurători de 2 L/h la 30 cm, o grădină de legume primește în 30–60 de minute cantitatea pentru o udare de vară. Folosește calculatorul pentru cazul tău.'),
    ('Pot folosi apă de ploaie pentru picurare?', 'Da, dar cu un filtru înainte de tuburi și, dacă butoiul e jos, cu o pompă mică sau cu picurători pentru presiune joasă.'),
]

ART_PvA = """<p>Nu există un sistem universal. Fiecare tip de plantă are sistemul lui.</p>
<div class="tw"><table class="t"><tr><th></th><th>Picurare</th><th>Aspersoare</th></tr>
<tr><td>Eficiența apei</td><td>Foarte mare (la rădăcină)</td><td>Medie (evaporare, vânt)</td></tr>
<tr><td>Potrivit pentru</td><td>Legume, flori, garduri vii, pomi</td><td>Gazon, suprafețe mari compacte</td></tr>
<tr><td>Boli ale frunzelor</td><td>Mai puține (frunzele rămân uscate)</td><td>Mai multe dacă uzi seara</td></tr>
<tr><td>Instalare</td><td>Simplă, la suprafață</td><td>Țevi îngropate pentru sisteme fixe</td></tr>
<tr><td>Presiune necesară</td><td>Mică</td><td>Mare (verifică presiunea de la robinet)</td></tr></table></div>
<h2>Picurare: pentru tot ce are rânduri</h2><p>Tubul cu picurători integrați (bandă sau țeavă) se întinde de-a lungul rândurilor. Pentru pomi și arbuști, picurătorii individuali, de 4–8 L/h, se pun în jurul trunchiului. Cu un reductor de presiune și un filtru, sistemul ține ani de zile.</p>
<h2>Aspersoare: pentru gazon</h2><p><strong>Aspersoarele fixe (spray)</strong> sunt pentru zone mici și înguste, aplică repede multă apă. <strong>Rotoarele</strong> acoperă distanțe mari și aplică apa încet, potrivit pentru gazoane mari și solul argilos.</p>
<h2>Combinația ideală</h2><p>Un programator cu două ieșiri sau un sistem cu electrovalve: o zonă cu aspersoare pentru gazon, una cu picurare pentru grădină și flori, fiecare cu programul ei.</p>""" + AFF_NOTE

ART_LEG = """<p>Un sistem de picurare pentru o grădină de 50–100 m² se montează într-o zi, fără săpături. Iată lista și pașii.</p>
<h2>Ce îți trebuie</h2><ul><li>Programator de robinet (opțional, dar îți schimbă vara)</li><li>Filtru și reductor de presiune (de obicei la 1–1,5 bar pentru picurare)</li><li>Țeavă principală (16 mm) de la robinet la grădină</li><li>Tub cu picurători integrați, la 30 cm, de-a lungul fiecărui rând</li><li>Conectori, coturi, teuri, dopuri de capăt și țăruși de fixare</li></ul>
<h2>Pașii</h2><ol><li><strong>Desenează grădina</strong> și măsoară lungimea rândurilor.</li><li><strong>La robinet:</strong> programator, filtru, reductor de presiune, în această ordine.</li><li><strong>Țeava principală</strong> trece perpendicular pe capetele rândurilor.</li><li><strong>Conectează tuburile cu picurători</strong> pe fiecare rând și pune dop la capăt.</li><li><strong>Spală sistemul</strong> cu dopurile deschise câteva minute, apoi închide-le.</li><li><strong>Testează:</strong> verifică că toți picurătorii dau apă și că nu ai scurgeri.</li><li><strong>Setează programul:</strong> folosește <a href="/">calculatorul</a> pentru durata potrivită.</li></ol>
<h2>Greșeli frecvente</h2><ul><li>Rânduri prea lungi: la capăt nu mai ajunge presiune. Respectă lungimea maximă din fișa tubului.</li><li>Fără filtru: picurătorii se înfundă în prima vară.</li><li>Iarna: golește sistemul și adu programatorul în casă înainte de îngheț.</li></ul>""" + AFF_NOTE

ART_PROG = """<p>Programatorul transformă un sistem de irigații într-unul automat. Iată tipurile și ce să alegi.</p>
<h2>Programator de robinet</h2><p>Se înșurubează direct pe robinet și funcționează pe baterii. Bun pentru o singură zonă sau două (modelele cu două ieșiri). Cel mai simplu și ieftin mod de a începe.</p>
<h2>Programator cu Wi-Fi sau Bluetooth</h2><p>Se controlează din aplicație: pornești udarea de la distanță, vezi istoricul și poți lega programul de prognoza meteo, ca să sară peste udare când plouă.</p>
<h2>Controler cu electrovalve</h2><p>Pentru sisteme fixe cu mai multe zone (gazon, picurare, flori). Un controler în casă comandă electrovalve îngropate în cutii. Este soluția pentru grădini mari.</p>
<h2>Senzorul de ploaie și de umiditate</h2><p>Un senzor de ploaie oprește programul când plouă. Senzorii de umiditate din sol sunt și mai precis: udă doar când solul s-a uscat.</p>
<h2>Ce alegi</h2><ul><li>Grădină mică, o zonă: programator de robinet.</li><li>Vrei control din telefon: programator Wi-Fi.</li><li>Gazon mare plus grădină: controler cu electrovalve și senzor de ploaie.</li></ul>
<div class="box">Înainte de îngheț, adu programatorul în casă și scoate bateriile. Apa rămasă în el îl poate crăpa.</div>""" + AFF_NOTE

SITE = {
    'name': 'IrigaSmart', 'domain': 'irigasmart.online',
    'c1': '#0a6e8a', 'c2': '#22a6b3', 'accent': '#9bdb4d',
    'mark': '<path d="M32 10c8 12 14 20 14 28a14 14 0 0 1-28 0c0-8 6-16 14-28z" fill="#fff"/><path d="M26 40a6 6 0 0 0 6 6" stroke="#9bdb4d" stroke-width="4" fill="none" stroke-linecap="round"/>',
    'tagline': 'Irigații pentru grădină explicate simplu: câtă apă, ce sistem și cum îl automatizezi.',
    'badges': ['Calculator apă și minute', 'Picurare și aspersoare', 'Apă de ploaie'],
    'nav': [('/', 'Calculator'), ('/picurare-sau-aspersoare.html', 'Picurare vs aspersoare'), ('/sistem-irigatii-gradina-legume.html', 'Montaj'), ('/ghiduri.html', 'Ghiduri')],
    'main_tool': 'Calculator irigații grădină',
    'side_title': 'Câte minute uzi?', 'side_text': 'Calculează apa și durata udării pentru grădina ta.',
    'about': '<p>IrigaSmart este un site independent despre irigarea grădinilor din România: sisteme prin picurare, aspersoare, programatoare și colectarea apei de ploaie, pentru veri tot mai secetoase.</p><p>Unele linkuri către magazine pot fi de afiliere și sunt marcate.</p>',
    'js': JS,
    'pages': [
        {'slug': 'index', 'title': 'Calculator irigații: câtă apă și câte minute uzi grădina', 'kind': 'tool', 'short': 'Calculator irigații', 'appcat': 'LifestyleApplication',
         'desc': 'Calculează câtă apă îi trebuie gazonului, grădinii de legume sau pomilor, câte minute pornești picurarea sau aspersoarele și cât te costă apa.',
         'h1': 'Calculator irigații: câtă apă și câte minute', 'toolname': 'Calculator irigații grădină',
         'lead': 'Alegi ce uzi, luna și sistemul. Afli necesarul de apă, durata fiecărei udări și costul pe lună.', 'body': INDEX_BODY, 'faq': FAQ},
        {'slug': 'picurare-sau-aspersoare', 'title': 'Irigare prin picurare sau aspersoare? Ce alegi', 'kind': 'article', 'short': 'Picurare sau aspersoare?',
         'desc': 'Comparație între irigarea prin picurare și aspersoare: eficiența apei, plante potrivite, presiune necesară și combinația ideală pentru grădină.',
         'h1': 'Picurare sau aspersoare: ce alegi pentru grădină', 'lead': 'Ce sistem pentru legume, gazon, flori și pomi.', 'body': ART_PvA},
        {'slug': 'sistem-irigatii-gradina-legume', 'title': 'Sistem de irigare prin picurare pentru legume: montaj', 'kind': 'article', 'short': 'Montaj picurare legume',
         'desc': 'Ce cumperi și cum montezi singur un sistem de irigare prin picurare pentru grădina de legume, pas cu pas, plus greșelile de evitat.',
         'h1': 'Cum montezi singur un sistem de picurare pentru legume', 'lead': 'Lista de cumpărături și cei 7 pași, într-o singură zi.', 'body': ART_LEG},
        {'slug': 'programator-irigatii', 'title': 'Programator irigații: de robinet, Wi-Fi sau electrovalve', 'kind': 'article', 'short': 'Programatoare de irigații',
         'desc': 'Tipurile de programatoare de irigații, senzorii de ploaie și umiditate și ce alegi pentru grădina ta.',
         'h1': 'Programatoare de irigații: ce tip alegi', 'lead': 'De la programatorul de robinet la controlerul cu mai multe zone.', 'body': ART_PROG},
    ]
}
