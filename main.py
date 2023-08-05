import pandas as pd
import streamlit as st

st.title("The Legend of Zelda: Tears of the Kingdom Shrine Walkthrough")

s = ['Anedamimik Shrine',
 'Apogek Shrine',
 'Bamitok Shrine',
 'Chichim Shrine',
 'Domizuin Shrine',
 'Ekochiu Shrine',
 'En-oma Shrine',
 'Eshos Shrine',
 'Eutoum Shrine',
 'Ga-Ahisas Shrine',
 'Ganos Shrine',
 'Gasas Shrine',
 'Gatakis Shrine',
 'Gatanisis Shrine',
 'Gemimik Shrine',
 'Gikaku Shrine',
 'Gutanbac Shrine',
 'Igashuk Shrine',
 'Igoshon Shrine',
 'Ihen-a Shrine',
 'Ijo-o Shrine',
 'Ikatak Shrine',
 'In-isa Shrine',
 'Irasak Shrine',
 'Ishodag Shrine',
 'Ishokin Shrine',
 'Isisim Shrine',
 'Iun-orok Shrine',
 'Jikais Shrine',
 'Jinodok Shrine',
 'Jiosin Shrine',
 'Jiotak Shrine',
 'Jirutagumac Shrine',
 'Jiukoum Shrine',
 'Jochi-ihiga Shrine',
 'Jochi-iu Shrine',
 'Jochisiu Shrine',
 'Jogou Shrine',
 'Jojon Shrine',
 'Joju-u-u Shrine',
 'Joku-u Shrine',
 'Joku-usin Shrine',
 'Joniu Shrine',
 'Jonsau Shrine',
 'Josiu Shrine',
 'Kadaunar Shrine',
 'Kahatanaum Shrine',
 'Kamatukis Shrine',
 'Kamizun Shrine',
 'Karahatag Shrine',
 'Kikakin Shrine',
 'Kimayat Shrine',
 'Kisinona Shrine',
 'Kitawak Shrine',
 'Kiuyoyou Shrine',
 'Kudanisar Shrine',
 'Kumamayn Shrine',
 'Kurakat Shrine',
 'Kyokugon Shrine',
 'Kyononis Shrine',
 'Makasura Shrine',
 'Makurukis Shrine',
 'Maoikes Shrine',
 'Marakuguc Shrine',
 'Marari-In Shrine',
 'Mayachideg Shrine',
 'Mayachin Shrine',
 'Mayahisik Shrine',
 'Mayak Shrine',
 'Mayam Shrine',
 'Mayamats Shrine',
 'Mayanas Shrine',
 'Mayaotaki Shrine',
 'Mayasiar Shrine',
 'Mayatat Shrine',
 'Mayaumekis Shrine',
 'Mayausiy Shrine',
 'Minetak Shrine',
 'Miryotanog Shrine',
 'Mogawak Shrine',
 'Mogisari Shrine',
 'Momosik Shrine',
 'Morok Shrine',
 'Moshapin Shrine',
 'Motsusis Shrine',
 'Musanokir Shrine',
 'Nachoyah Shrine',
 'Natak Shrine',
 'Ninjis Shrine',
 'Nouda Shrine',
 'O-ogim Shrine',
 'Orochium Shrine',
 'Oromuwak Shrine',
 'Oshozan-u Shrine',
 'Otak Shrine',
 'Otutsum Shrine',
 'Pupunke Shrine',
 'Rakakudaj Shrine',
 'Rakashog Shrine',
 'Rasitakiwak Shrine',
 'Rasiwak Shrine',
 'Ren-iz Shrine',
 'Riogok Shrine',
 'Rotsumamu Shrine',
 'Runakit Shrine',
 'Rutafu-um Shrine',
 'Sahirow Shrine',
 'Sakunbomar Shrine',
 'Sepapa Shrine',
 'Serutabomac Shrine',
 'Sibajitak Shrine',
 'Sifumim Shrine',
 'Sihajog Shrine',
 'Sikukuu Shrine',
 'Simosiwak Shrine',
 'Sinakawak Shrine',
 'Sinatanika Shrine',
 'Sisuran Shrine',
 'Sitsum Shrine',
 'Siwakama Shrine',
 'Siyamotsus Shrine',
 'Sonapan Shrine',
 'Soryotanog Shrine',
 'Suariwak Shrine',
 'Susub Shrine',
 'Susuyai Shrine',
 'Tadarok Shrine',
 'Tajikats Shrine',
 'Taki-ihaban Shrine',
 'Taninoud Shrine',
 'Taunhiy Shrine',
 'Tauyosipun Shrine',
 'Tenbez Shrine',
 'Teniten Shrine',
 'Tenmaten Shrine',
 'Timawak Shrine',
 'Tokiy Shrine',
 'Tsutsu-um Shrine',
 'Tukarok Shrine',
 'Turakamik Shrine',
 'Turakawak Shrine',
 'Ukoojisi Shrine',
 'Ukouh Shrine',
 'Usazum Shrine',
 'Utojis Shrine',
 'Utsushok Shrine',
 'Wao-os Shrine',
 'Yamiyo Shrine',
 'Yansamin Shrine',
 'Yomizuk Shrine',
 'Zakusu Shrine',
 'Zanmik Shrine']

u = ['https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23729987/anedamimik-shrine-solution-a-retraced-path-puzzle-chest',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23730081/apogek-shrine-wings-on-the-wind-puzzle-solution-chest',
 'https://www.polygon.com/e/23494489',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23732635/chichim-shrine-solution-gerudo-desert-ancient-prison-ruins',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23724576/domizuin-shrine-a-prone-pathway-solution-puzzle-chest',
 'https://www.polygon.com/e/23472888',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23733312/en-oma-shrine-lake-hylia-puzzle-solution-chest',
 'https://www.polygon.com/e/23471220',
 'https://www.polygon.com/e/23500417',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23733512/ga-ahisas-shrine-solution-puzzle-chest',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23734862/ganos-shrine-puzzle-solution-chest-tabantha-sky-crystal-quest',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23730080/gasas-shrine-well-timed-cuts-solution-puzzle-reward',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23728530/gatakis-shrine-solution-puzzle-chest',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23733404/gatanisis-shrine-solution-puzzle-chest',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23727605/gemimik-shrine-solution-puzzle-chest',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23751173/gikaku-shrine-location-sky-mine-crystal-walkthrough-totk',
 'https://www.polygon.com/e/23466548',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23745317/lomei-labyrinth-island-walkthrough-igashuk-mogisari-shrine-puzzle-solution',
 'https://www.polygon.com/e/23471167',
 'https://www.polygon.com/e/23470618',
 'https://www.polygon.com/e/23474131',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23744355/ikatak-shrine-location-gisa-crater-crystal-quest',
 'https://www.polygon.com/e/23464190',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23750876/irasak-shrine-location-walkthrough-puzzle-solution',
 'https://www.polygon.com/e/23467127',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23729010/ishokin-shrine-ride-the-giant-horse-solution-puzzle-chest',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23733507/isisim-shrine-solution-puzzle-chest',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23743693/iun-orok-shrine-right-roll-location-walkthrough',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23736198/jikais-shrine-location-jailbreak-walkthrough',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23730250/jinodok-shrine-solution-puzzle-chest',
 'https://www.polygon.com/e/23466626',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23744105/jiotak-shrine-location-walkthrough-isle-rabac-gallery-totk',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23723241/jirutagumac-shrine-puzzle-solution-chest',
 'https://www.polygon.com/e/23471083',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23730082/jochi-ihiga-shrine-solution-puzzle-reward-crystal',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23735958/jochi-iu-shrine-courage-pluck-location-walkthrough',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23743924/jochisiu-shrine-location-keys-born-water-walkthrough-totk',
 'https://www.polygon.com/e/23509369',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23751050/jojon-shrine-location-proving-grounds-rotation',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23727774/joju-u-u-shrine-solution-building-bridges-chest-puzzle',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23751241/joku-u-shrine-location-walkthrough-totk',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23743805/joku-usin-shrine-location-proving-grounds-short-circuit',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23743748/joniu-shrine-location-ralis-channel-crystal-walkthrough-totk',
 'https://www.polygon.com/e/23467000',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23728701/josiu-shrine-solution-north-necluda-sky-crystal-puzzle-chest',
 'https://www.polygon.com/e/23481405',
 'https://www.polygon.com/e/23474024',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23734853/kamatukis-shrine-solution-puzzle-chest',
 'https://www.polygon.com/e/23470641',
 'https://www.polygon.com/e/23477594',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23727775/kikakin-shrine-solution-puzzle-chests-shining-in-darkness',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23688371/kimayat-shrine-proving-grounds-smash-solution-puzzle-chest',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23726021/kisinona-shrine-wind-power-solution-puzzle-chest',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23735784/kitawak-shrine-location-upward-forward-walkthrough',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23724504/kiuyoyou-shrine-solution-puzzle-chest',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23743989/kudanisar-shrine-location-bridging-sands',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23731058/kumamayn-shrine-solution-east-necluda-sky-crystal-puzzle-chest',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23744473/kurakat-shrine-location-dyeing-to-find-it-puzzle-reward-solution',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23730180/kyokugon-shrine-solution-alignment-of-circles',
 'https://www.polygon.com/e/23467028',
 'https://www.polygon.com/e/23470981',
 'https://www.polygon.com/e/23475386',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23730038/maoikes-shrine-solution-puzzle-chest',
 'https://www.polygon.com/e/23472886',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23736138/marari-in-shrine-eventide-pirate-hideout-location-walkthrough',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23733509/mayachideg-shrine-solution-puzzle-chest',
 'https://www.polygon.com/e/23471072',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23753740/mayahisik-shrine-location-walkthrough-totk',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23730404/mayak-shrine-solution-puzzle-chest',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23725446/mayam-shrine-solution-in-zelda-tears-of-the-kingdom',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23743918/mayamats-shrine-a-route-for-a-ball-location-walkthrough',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23730248/mayanas-shrine-solution-ice-guides-you-puzzle',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23694023/north-lomei-labyrinth-mayaotaki-tenbez-shrine-solution-puzzle-maze',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23753873/mayasiar-shrine-location-starview-island-walkthrough-lights-mirrors',
 'https://www.polygon.com/e/23479268',
 'https://www.polygon.com/e/23474271',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23728717/mayausiy-shrine-building-blocks-solution-puzzle-chest',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23746736/minetak-shrine-location-reward-puzzle-walkthrough',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23734195/miryotanog-shrine-solution-puzzle-chest',
 'https://www.polygon.com/e/23466661',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23745317/lomei-labyrinth-island-walkthrough-igashuk-mogisari-shrine-puzzle-solution',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23732849/momosik-shrine-puzzle-solution-chest',
 'https://www.polygon.com/e/23466760',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23745664/moshapin-shrine-location-lake-intenoch-cave-walkthrough-totk',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23737222/south-lomei-labyrinth-motsusis-siyamotsus-shrine-solution-puzzle-maze',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23724754/musanokir-shrine-solution-puzzle-chest',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23702514/nachoyah-shrine-solution-puzzle-chest',
 'https://www.polygon.com/e/23477077',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23751222/ninjis-shrine-macas-special-place-puzzle-solution-reward',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23742939/nouda-shrine-proving-grounds-intermediate-location-walkthrough',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23745879/o-ogim-shrine-location-walkthrough-solution-reward',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23723101/orochium-shrine-puzzle-solution-chest',
 'https://www.polygon.com/e/23472776',
 'https://www.polygon.com/e/23518316',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23746807/otak-shrine-location-proving-grounds-traps-walkthrough-totk',
 'https://www.polygon.com/e/23518271',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23752305/pupunke-shrine-pretty-stone-five-golden-apples-location-walkthrough',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23752318/rakakudaj-shrine-location-gerudo-canyon-crystal-walkthrough-totk',
 'https://www.polygon.com/e/23481260',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23730069/rasitakiwak-shrine-solution-puzzles-chest',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23745409/rasiwak-shrine-location-reward-puzzle-walkthrough',
 'https://www.polygon.com/e/23517961',
 'https://www.polygon.com/e/23472031',
 'https://www.polygon.com/e/23513643',
 'https://www.polygon.com/e/23472861',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23745287/rutafu-um-shrine-location-walkthrough',
 'https://www.polygon.com/e/23480322',
 'https://www.polygon.com/e/23517015',
 'https://www.polygon.com/e/23475701',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23750297/serutabomac-shrine-location-walkthrough',
 'https://www.polygon.com/e/23476459',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23729942/sifumim-shrine-solution-puzzle-chest',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23730202/sihajog-shrine-raurus-blessing-puzzle-reward-diamond-skydiving',
 'https://www.polygon.com/e/23474324',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23752970/simosiwak-shrine-location-proving-grounds-lights-out-walkthrough-totk',
 'https://www.polygon.com/e/23470540',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23742408/sinatanika-shrine-location-combat-training-sneakstrike-walkthrough-totk',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23754131/sisuran-shrine-north-hebra-mountains-crystal-location-walkthrough',
 'https://www.polygon.com/e/23476461',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23749941/siwakama-shrine-solution-puzzle-chest',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23737222/south-lomei-labyrinth-motsusis-siyamotsus-shrine-solution-puzzle-maze',
 'https://www.polygon.com/e/23470530',
 'https://www.polygon.com/e/23479269',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23749972/suariwak-shrine-location-yiga-clan-exam-map-walkthrough',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23742806/susub-shrine-location-walkthrough-solution-reward',
 'https://www.polygon.com/e/23470521',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23735882/tadarok-shrine-fire-water-location-walkthrough',
 'https://www.polygon.com/e/23466952',
 'https://www.polygon.com/e/23475090',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23746685/taninoud-shrine-location-east-hebra-sky-crystal-walkthrough-totk',
 'https://www.polygon.com/e/23517821',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23742455/tauyosipun-shrine-forward-backward-location',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23694023/north-lomei-labyrinth-mayaotaki-tenbez-shrine-solution-puzzle-maze',
 'https://www.polygon.com/e/23471193',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23742691/tenmaten-shrine-elma-knolls-well-location-walkthrough',
 'https://www.polygon.com/e/23474322',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23750256/tokiy-shrine-solution-puzzle-chest-quest',
 'https://www.polygon.com/e/23471223',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23722374/tukarok-shrine-solution-puzzle-chest',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23734302/turakamik-shrine-puzzle-solution-chest',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23743961/turakamik-shrine-location-stacking-path-chest',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23725369/ukoojisi-shrine-solution-puzzle-chest',
 'https://www.polygon.com/e/23464158',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23753060/usazum-shrine-satori-mountain-crystal-location-walkthrough',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23742599/utojis-shrine-location-legend-soaring-spear-walkthrough',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23728854/utsushok-shrine-solution-puzzle-chest',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23742801/wao-os-shrine-lever-power-white-birds-guidance-west-lake-totori-cave-location-walkthrough',
 'https://www.polygon.com/e/23466559',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23745186/yansamin-shrine-proving-grounds-low-gravity-location-walkthrough',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23730517/yomizuk-shrine-solution-puzzle-chest-diamond',
 'https://www.polygon.com/zelda-tears-of-the-kingdom-guide/23742622/zakusu-shrine-proving-grounds-ascensionhigh-spring-light-rings-quest-location',
 'https://www.polygon.com/e/23477634']

y = ['https://www.youtube.com/watch?v=J0U1K_RgkNQ&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=86&pp=iAQB',
 'https://www.youtube.com/watch?v=2Y89XGiSDuo&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=80&pp=iAQB',
 'https://www.youtube.com/watch?v=xnxrRjLyxwg&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=79&pp=iAQB',
 'https://www.youtube.com/watch?v=yMxgXCtzw1o&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=69&pp=iAQB',
 'https://www.youtube.com/watch?v=6EtuoWomqP4&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=1&pp=iAQB',
 'https://www.youtube.com/watch?v=-GIPGcJAPE8&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=23&pp=iAQB',
 'https://www.youtube.com/watch?v=sPewZMThbWk&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=73&pp=iAQB',
 'https://www.youtube.com/watch?v=MARP9Ji0vhk&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=2&pp=iAQB',
 'https://www.youtube.com/watch?v=bevmQfgc-uQ&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=88&pp=iAQB',
 'https://www.youtube.com/watch?v=fOx1apO-dpY&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=47&pp=iAQB',
 'https://www.youtube.com/watch?v=1I5de2G9rzA&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=48&pp=iAQB',
 'https://www.youtube.com/watch?v=ygT5xwKn97g',
 'https://www.youtube.com/watch?v=1K3X9XaNeac&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=62&pp=iAQB',
 'https://www.youtube.com/watch?v=ZN-fqVwilyo&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=78&pp=iAQB',
 'https://www.youtube.com/watch?v=zHpjb4Sme20&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=43&pp=iAQB',
 'https://www.youtube.com/watch?v=GRJDq1f74r0&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=89&pp=iAQB',
 'https://www.youtube.com/watch?v=bhYs5RGqAE4&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=3&pp=iAQB',
 'https://www.youtube.com/watch?v=7mHObbp-UIg&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=90&pp=iAQB',
 'https://www.youtube.com/watch?v=bK0Lt-0wjU8&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=54&pp=iAQB',
 'https://www.youtube.com/watch?v=_7xmCqSPjhY&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=67&pp=iAQB',
 'https://www.youtube.com/watch?v=cooewA6f2RU&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=77&pp=iAQB',
 'https://www.youtube.com/watch?v=_o9NIoDih5U&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=91&pp=iAQB',
 'https://www.youtube.com/watch?v=iPomp_bj8Ps&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=4&pp=iAQB',
 'https://www.youtube.com/watch?v=4w0InqZ24bY&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=70&pp=iAQB',
 'https://www.youtube.com/watch?v=WqQitMhfeZw&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=5&pp=iAQB',
 'https://www.youtube.com/watch?v=j28qyNzzI-4',
 'https://www.youtube.com/watch?v=lVX2wsCVtmg&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=87&pp=iAQB',
 'https://www.youtube.com/watch?v=AsYtdkeD7Pc&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=92&pp=iAQB',
 'https://www.youtube.com/watch?v=gOjJGWyV2-s&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=51&pp=iAQB',
 'https://www.youtube.com/watch?v=MHEcoS27Ba0&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=6&pp=iAQB',
 'https://www.youtube.com/watch?v=ZztJtsUFkxg&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=7&pp=iAQB',
 'https://www.youtube.com/watch?v=qg4BXjWEHPA&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=65&pp=iAQB',
 'https://www.youtube.com/watch?v=dSTB3qxsuUs&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=49&pp=iAQB',
 'https://www.youtube.com/watch?v=vlMdczazn6w&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=61&pp=iAQB',
 'https://www.youtube.com/watch?v=F-es-R3phvQ&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=93&pp=iAQB',
 'https://www.youtube.com/watch?v=do7as6PGs8o',
 'https://www.youtube.com/watch?v=Ae4s_RS03LY&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=60&pp=iAQB',
 'https://www.youtube.com/watch?v=WFUSkTealx4&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=94&pp=iAQB',
 'https://www.youtube.com/watch?v=WosSeCQIp80&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=95&pp=iAQB',
 'https://www.youtube.com/watch?v=CpDMouuK1Xo&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=96&pp=iAQB',
 'https://www.youtube.com/watch?v=i9mzMm5sU_c&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=55&pp=iAQB',
 'https://www.youtube.com/watch?v=2GhXjZy1I8g',
 'https://www.youtube.com/watch?v=CKO-w5rok00&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=97&pp=iAQB',
 'https://www.youtube.com/watch?v=Ud-SpbkorNo&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=8&pp=iAQB',
 'https://www.youtube.com/watch?v=EOt_f-iLVlQ&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=24&pp=iAQB',
 'https://www.youtube.com/watch?v=-uOEp-ddtN0&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=25&pp=iAQB',
 'https://www.youtube.com/watch?v=oUggbL1uH6A&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=36&pp=iAQB',
 'https://www.youtube.com/watch?v=M5Y4e6GDy_k&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=44&pp=iAQB',
 'https://www.youtube.com/watch?v=ZPGP8wALtvQ',
 'https://www.youtube.com/watch?v=tzWVyB396yk&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=71&pp=iAQB',
 'https://www.youtube.com/watch?v=AJoVO9hhZOI&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=53&pp=iAQB',
 'https://www.youtube.com/watch?v=oF6c6emk0m0&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=98&pp=iAQB',
 'https://www.youtube.com/watch?v=l9aSG52bonM&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=64&pp=iAQB',
 'https://www.youtube.com/watch?v=6QAIIFz4hyI&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=99&pp=iAQB',
 'https://www.youtube.com/watch?v=SSK39uHwkXA&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=26&pp=iAQB',
 'https://www.youtube.com/watch?v=brVddDvSwJg&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=100&pp=iAQB',
 'https://www.youtube.com/watch?v=5vAK9huqOdg&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=37&pp=iAQB',
 'https://www.youtube.com/watch?v=YX4Tff8D26U&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=58&pp=iAQB',
 'https://www.youtube.com/watch?v=6os0sM77_4U&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=101&pp=iAQB',
 'https://www.youtube.com/watch?v=3RtV9t4iMyQ&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=9&pp=iAQB',
 'https://www.youtube.com/watch?v=ksctZN_mdK4&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=10&pp=iAQB',
 'https://www.youtube.com/watch?v=X6rnquvh9Ug&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=27&pp=iAQB',
 'https://www.youtube.com/watch?v=ItXHVFwHXAc&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=42&pp=iAQB',
 'https://www.youtube.com/watch?v=eSIZJMiMycg&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=123&pp=iAQB',
 'https://www.youtube.com/watch?v=qIbjg1VAuxw&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=102&pp=iAQB',
 'https://www.youtube.com/watch?v=Vf3hlU-kTYA&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=103&pp=iAQB',
 'https://www.youtube.com/watch?v=UnOzqcFffKI&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=11&pp=iAQB',
 'https://www.youtube.com/watch?v=AjC8cYGq07o',
 'https://www.youtube.com/watch?v=ofjq8O8HLm0&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=76&pp=iAQB',
 'https://www.youtube.com/watch?v=egG9jFRZ7To',
 'https://www.youtube.com/watch?v=nKkIzhP_KBA&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=104&pp=iAQB',
 'https://www.youtube.com/watch?v=PzCKGOezOjo&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=56&pp=iAQB',
 'https://www.youtube.com/watch?v=uCQLMtyzaN8&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=105&pp=iAQB',
 'https://www.youtube.com/watch?v=Y_HjfkzxI6k&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=106&pp=iAQB',
 'https://www.youtube.com/watch?v=wPP-_apV9GI&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=107&pp=iAQB',
 'https://www.youtube.com/watch?v=2AtHpsiSJ-U&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=35&pp=iAQB',
 'https://www.youtube.com/watch?v=DkTqUyAtKGE&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=12&pp=iAQB',
 'https://www.youtube.com/watch?v=BKWtpwXW-Ng&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=108&pp=iAQB',
 'https://www.youtube.com/watch?v=zVLGfoCDVKY&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=109&pp=iAQB',
 'https://www.youtube.com/watch?v=VmJbRLDZmT8&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=66&pp=iAQB',
 'https://www.youtube.com/watch?v=Ot9_TN82d60&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=124&pp=iAQB',
 'https://www.youtube.com/watch?v=R8WhieCz1yw&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=110&pp=iAQB',
 'https://www.youtube.com/watch?v=W6VadYdFWzA&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=13&pp=iAQB',
 'https://www.youtube.com/watch?v=uTlgdFbJJmQ&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=84&pp=iAQB',
 'https://www.youtube.com/watch?v=uwkP_4DhWLw&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=111&pp=iAQB',
 'https://www.youtube.com/watch?v=0qirfge4vmA&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=45&pp=iAQB',
 'https://www.youtube.com/watch?v=AgdRbP46f-0&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=14&pp=iAQB',
 'https://www.youtube.com/watch?v=r1hbViDYc8A',
 'https://www.youtube.com/watch?v=sYOVkxtoDY0&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=46&pp=iAQB',
 'https://www.youtube.com/watch?v=dFFPtNJTU1E&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=112&pp=iAQB',
 'https://www.youtube.com/watch?v=kab_-F9WW2Y&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=59&pp=iAQB',
 'https://www.youtube.com/watch?v=G9rbFMlIZUM&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=15&pp=iAQB',
 'https://www.youtube.com/watch?v=cILJBK0zFvg',
 'https://www.youtube.com/watch?v=fVZMMM3ntQ4&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=113&pp=iAQB',
 'https://www.youtube.com/watch?v=iBVg-ksXcq8&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=114&pp=iAQB',
 'https://www.youtube.com/watch?v=hWgmXyu-1y8&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=115&pp=iAQB',
 'https://www.youtube.com/watch?v=eA1x31uM3zM&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=116&pp=iAQB',
 'https://www.youtube.com/watch?v=XI8nTlex4so&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=63&pp=iAQB',
 'https://www.youtube.com/watch?v=3TbJymY-6lY',
 'https://www.youtube.com/watch?v=Jn4EAADIqLU&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=68&pp=iAQB',
 'https://www.youtube.com/watch?v=Do80w5oLc_Q',
 'https://www.youtube.com/watch?v=rqhc58g4a4c&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=125&pp=iAQB',
 'https://www.youtube.com/watch?v=KWxC4dCkTHE&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=40&pp=iAQB',
 'https://www.youtube.com/watch?v=_OQJsA0Vf_A',
 'https://www.youtube.com/watch?v=tIuCRzFVXWU&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=16&pp=iAQB',
 'https://www.youtube.com/watch?v=pUpg-DYeh_I&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=126&pp=iAQB',
 'https://www.youtube.com/watch?v=AIi74LFffdo&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=83&pp=iAQB',
 'https://www.youtube.com/watch?v=QOt5DJiTCPI&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=52&pp=iAQB',
 'https://www.youtube.com/watch?v=Gj2Wu5tJrmQ&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=28&pp=iAQB',
 'https://www.youtube.com/watch?v=D3VF9OxrZ5M&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=127&pp=iAQB',
 'https://www.youtube.com/watch?v=IFBTDipMteI&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=82&pp=iAQB',
 'https://www.youtube.com/watch?v=XtMsv3mGgkE&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=117&pp=iAQB',
 'https://www.youtube.com/watch?v=h9qr5ZMI41s&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=128&pp=iAQB',
 'https://www.youtube.com/watch?v=d_DJadNIWMM',
 'https://www.youtube.com/watch?v=irk0FMn27XQ&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=50&pp=iAQB',
 'https://www.youtube.com/watch?v=ObU0wMy-wac&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=17&pp=iAQB',
 'https://www.youtube.com/watch?v=r0HtjjOSq4s&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=81&pp=iAQB',
 'https://www.youtube.com/watch?v=w4bm-tLN11k&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=118&pp=iAQB',
 'https://www.youtube.com/watch?v=2gSeDEcFwNQ',
 'https://www.youtube.com/watch?v=-scP9w12aKo&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=129&pp=iAQB',
 'https://www.youtube.com/watch?v=nv1QbLI1AQ8&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=130&pp=iAQB',
 'https://www.youtube.com/watch?v=7Q0QlA4KLMo&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=119&pp=iAQB',
 'https://www.youtube.com/watch?v=_CEV3UJ3i7M',
 'https://www.youtube.com/watch?v=b9vzf7sOq5Q&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=85&pp=iAQB',
 'https://www.youtube.com/watch?v=eJVWAjodiC0&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=72&pp=iAQB',
 'https://www.youtube.com/watch?v=H1XlTPOTvh4&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=29&pp=iAQB',
 'https://www.youtube.com/watch?v=g8xHoJAAhKc&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=120&pp=iAQB',
 'https://www.youtube.com/watch?v=gG-CbZYQcFg&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=39&pp=iAQB',
 'https://www.youtube.com/watch?v=5Hazlxf4aKM&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=30&pp=iAQB',
 'https://www.youtube.com/watch?v=pTCgjp5hZY8&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=33&pp=iAQB',
 'https://www.youtube.com/watch?v=xqzvNlxpM7I&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=18&pp=iAQB',
 'https://www.youtube.com/watch?v=0zZ3yRisWTk&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=131&pp=iAQB',
 'https://www.youtube.com/watch?v=tzLw5zxeCMw&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=34&pp=iAQB',
 'https://www.youtube.com/watch?v=ziHf40_27tc&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=19&pp=iAQB',
 'https://www.youtube.com/watch?v=OIZSr0Zby7Y&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=121&pp=iAQB',
 'https://www.youtube.com/watch?v=Y7H-nC99Y1c&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=31&pp=iAQB',
 'https://www.youtube.com/watch?v=lhI7T_PJWus&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=74&pp=iAQB',
 'https://www.youtube.com/watch?v=gBi8sFSat1E&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=41&pp=iAQB',
 'https://www.youtube.com/watch?v=uIsFXIHZH6w&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=20&pp=iAQB',
 'https://www.youtube.com/watch?v=Y1YrG-feau8&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=132&pp=iAQB',
 'https://www.youtube.com/watch?v=KbUpj6Vm5dA&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=32&pp=iAQB',
 'https://www.youtube.com/watch?v=xaDXe1YoJEU&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=133&pp=iAQB',
 'https://www.youtube.com/watch?v=RoonS60l_ms&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=21&pp=iAQB',
 'https://www.youtube.com/watch?v=m5Dm7oSiFro&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=134&pp=iAQB',
 'https://www.youtube.com/watch?v=vT5oImFvcnw&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=75&pp=iAQB',
 'https://www.youtube.com/watch?v=acGhrXEGcUI&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=122&pp=iAQB',
 'https://www.youtube.com/watch?v=WnzrFozlLyA&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=135&pp=iAQB',
 'https://www.youtube.com/watch?v=XxbieBMH44M&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=22&pp=iAQB',
 'https://www.youtube.com/watch?v=-KJLhnDAr30&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=57&pp=iAQB',
 'https://www.youtube.com/watch?v=uKNO4GBJHRI&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=136&pp=iAQB',
 'https://www.youtube.com/watch?v=xCHtQ2pVCMc&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=137&pp=iAQB',
 'https://www.youtube.com/watch?v=lSvql_mqRlU&list=PLqBTiHv6qMa4mbiwb22Ue3apVl3r1yw1p&index=38&pp=iAQB']






@st.cache_resource
def show_maps(sky_or_surface):
    if sky_or_surface == "Surface":
        st.write("- Surface Map:")
        st.image("shrine_surface.png")
    if sky_or_surface == "Sky":
        st.write("- Sky Map:")
        st.image("shrine_sky.png")

sky_or_surface = st.selectbox("Select surface or sky map", options = ['None', 'Surface', "Sky"])
show_maps(sky_or_surface)

df = pd.DataFrame(zip(s, u, y), columns = ['shrine', 'url', 'Youtube'])
list_of_shrines = list(df['shrine'].values)
list_of_shrines.sort()
shrine_url_dict = dict(zip(df['shrine'].values, df['url'].values))
shrine_yt_dict = dict(zip(df['shrine'].values, df['Youtube'].values))

shrines_selected = st.multiselect("Select shrine(s):", options = list_of_shrines)
if shrines_selected:
    for shrine in shrines_selected:
        st.subheader(shrine)
        st.write(f"- Guide: {shrine_url_dict.get(shrine)}")
        st.write("- YouTube Walkthrough:")
        st.video(shrine_yt_dict.get(shrine))
        st.write("----")