#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from rsactftool.lib.keys_wrapper import PrivateKey


def attack(attack_rsa_obj, publickey, cipher=[]):
    """ Search for previously used primes in CTFs
    """
    primes = [
        108082147276398906822234149167480016132157014049560913761488880190018027488520386318253742675423286348552334110023434741671427911613197684395221211646299519273129194692306445874938199068586137486874290442314459278649345469626426790676801658394799404284116771456479272808343825651929906737811050557836671896732124546721747709022607151231423494815945385193624295868730390462068156825588342737037490320356361648437686599733,
        108082147276398906822234149167480016132157014049560913761488880190018027488520386318253742675423286348552334110023434741671427911613197684395221211646299519273129194692306445874938199068586137486874290442314459278649345469626426790676801658394799404284116771456479272808343825651929906737811050557836671896732124546721747709022607151231423494815945385193624295868730390462068156825588342737037490320356361648437686598461,
        108082147276398906822234149167480016132157014049560913761488880190018027488520386318253742675423286348552334110023434741671427911613197684395221211646299519273129194692306445874938199068586137486874290442314459278649345469626426790676801658394799404284116771456479272808343825651929906737811050557836671896732124546721747709022607151231423494815945385193624295868730390462068156825588342737037490320356361648437686597791,
        108082147276398906822234149167480016132157014049560913761488880190018027488520386318253742675423286348552334110023434741671427911613197684395221211646299519273129194692306445874938199068586137486874290442314459278649345469626426790676801658394799404284116771456479272808343825651929906737811050557836671896732124546721747709022607151231423494815945385193624295868730390462068156825588342737037490320356361648437686600843,
        6703903965361517118576511528025622717463828698514771456694902115718276634989944955753407851598489976727952425488221391817052769267904281935379659980013749,
        13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903820008890319855427587165500997237443558735689450602365103,
        4101860217206195486319508931988944464741665503169699281154625914180099350459859416508157842908810493659777848990372055112637980426665995893689191266676993,
        4101860217206195486319508931988944464741665503169699281154625914180099350459859416508157842908810493659777848990372055112637980426665995893689191266677141,
        4101860217206195486319508931988944464741665503169699281154625914180099350459859416508157842908810493659777848990372055112637980426665995893689191266677279,
        4165938907260954640804986514555496835723686162893011508104816859692320046868363019435944953520658898678455053432699809898947934756189120526030787871227407,
        4165938907260954640804986514555496835723686162893011508104816859692320046868363019435944953520658898678455053432699809898947934756189120526030787871227587,
        4165938907260954640804986514555496835723686162893011508104816859692320046868363019435944953520658898678455053432699809898947934756189120526030787871227863,
        12643740637395110652894262209502063899047520218436247735878188180335985789877601396069401620713231058940443043891453952791936466967524033214476598572706213,
        12217494205780318874865198006759446969679921137474855298485716817925925911890415286181103665676748660959871257808447814451048738105000263500773868071134927,
        12753003603072550531018654801465540625925587065270735249200707034221342553612566510512289220382168917762612389041102258111324579759414416978278947259367203,
        11512221259968944711215688757058402596735146070663731484166937019905962795560024445608131301476308525203431567566930188520189544071868201113560261699518477,
        120154561482812169366431552175315487829790853533514455083187141150401404579723989466386713554692826031183462112641793395815695957964420754471645865010199918851008631038679685035857813488382170765657628252079464574576993595350214255290554756868269962991079417299897885957935578968328491235168443836989742332343,
        164184701914508585475304431352949988726937945291,
        123722643358410276082662590855480232574295213977,
        1367950959033448694251101693351971454646908585982174247214456588106744480223502924899594970200721567086593256490339820357729417073968911473368284373028327,
        1873061312526431600198418914726418187289872964131683141580934527253790685014095254664971230592314176869517383698550622907346640404434127554775124138006963,
        72432241732033981541049204016745025006867436329489703868293535625696723664804764149457845005290546241606890061226796845022216057745054630401792003744462109,
        90126444730029710403645054775061222054869762216009860614264509250054875494146740846632769652653539286830798492363476860052054761040294014518933023714223427,
        279125332373073513017147096164124452877,
        295214597363242917440342570226980714417,
        25478326064937419292200172136399497719081842914528228316455906211693118321971399936004729134841162974144246271486439695786036588117424611881955950996219646807378822278285638261582099108339438949573034101215141156156408742843820048066830863814362379885720395082318462850002901605689761876319151147352730090957556940842144299887394678743607766937828094478336401159449035878306853716216548374273462386508307367713112073004011383418967894930554067582453248981022011922883374442736848045920676341361871231787163441467533076890081721882179369168787287724769642665399992556052144845878600126283968890273067575342061776244939,
        783420406144696097385833069281677113,
        783756020423148789078921701951691559,
        31834349,
        48670331,
        19193025210159847056853811703017693,
        17357677172158834256725194757225793,
        279125332373073513017147096164124452877,
        295214597363242917440342570226980714417,
        42727,
        58757,
        123722643358410276082662590855480232574295213977,
        164184701914508585475304431352949988726937945291,
        800644567978575682363895000391634967,
        83024947846700869393771322159348359271173,
        37024794671302122535260220812153587643,
        272573531366295567443756143024197333707,
        21563957808398119329545349513312897291720371794644161565433575994922624494866014735925135594671402533520230648695949559828278766299067426136066601816643711,
        22708406967509416561081471369947020796745437757938294005271339336356008357234294069698063747451399564794968797317330497407167861251551902204973484175503837,
        144299940222848685214153733110344660304144248927927225494186904499495592842937728938865184611511914233674465357703431948804720019559293726714685845430627084912877192848598444717376108179511822902563959186098293320939635766298482099885173238182915991321932102606591240368970651488289284872552548559190434607447,
        144245059483864997316184517203073096336312163518349447278779492969760750146161606776371569522895088103056082865212093431805166968588430946389831338526998726900084424430828957236538023320369476765118148928194401317313951462365588911048597017242401293395926609382786042879520305147467629849523719036035657146109,
        26440615366395242196516853423447,
        32581479300404876772405716877547,
        27038194053540661979045656526063,
        31267675316206058850450140119274819751417791661635697504813240447984629079490652100735044733540913861142747523203435425061407513320468637503374655392825781473928382075249940537540518803447705157748005302692062548318810509906583495199574613016294007136437402473510780242916703476437678742060227320715065951829792345046885904400712909744723822283218325063910405248903702979799406800950896480067506026510838938457917561846489922757260048427449921729671259609502925944554834113384775414185570194511576885758113751887157223120097006977944365867967544959413407725601588176723859982645734322192561519871486442323167074933639,
        43068974121995373755259728623203756276151708711206529799133972499770311973917522370590279232720654505974288964559409201661353918115651149664716192367955840217357608436100090406769463686865453605648714294729259644629396177958653095754824288389624580579733807505133514369658203797575477437151706954894720485223,
        698962359293224388508528504293868295849536117911029511500535686265628116126035273937376653818042771965856143346411321978169984196703587737297011635332863244713959616825373265069482088742784543259349452001104153825865595450998374567435519147735270488504450983670922877905525006233437224249682098320961706073951,
        4911154640312831735300579932662636306005188439240020352879,
        5858530077012370931106950309549472688326371985155604622439,
        1451135465007329936687682012556458198263354033267,
        1283383279909541494981671251013593566543423047599,
        289260226283275563579648656678444936057,
        288180072604771133716023733756993741403,
        32158763574926282399690427421751598974822750157866002942864427634852437380540017586451493854661729909380518733649186624385206737336324813109500237603304026009112696565510846849987937423619262973393969175056759821652138869783215378169757835283584660846583208812725733839059137580944002686113912792569631796916069732431775599320458346937859589815497525828622622652165709271152246464728489927670696601016248559515951932154686633599100945314921834227324381958751184684979824241375253606863601895383658582486045363570755445629865194046700806542078378801136397577730247660070033517187439537339428288763342861366560261446073,
        32158763574926282399690427421751598974822750157866002942864427634852437380540017586451493854661729909380518733649186624385206737336324813109500237603304026009112696565510846849987937423619262973393969175056759821652138869783215378169757835283584660846583208812725733839059137580944002686113912792569631796916069732431775599320458346937859589815497525828622622652165709271152246464728489927670696601016248559515951932154686633599100945314921834227324381958751184684979824241375253606863601895383658582486045363570755445629865194046700806542078378801136397577730247660070033517187439537339428288763342861366560261414507,
        30555909537318327326226067108345484260972616392831008890345613182167918843881096961410781393695029449357707848545288220880122374798556583885387343041975279297622137379354808942799947266338126600859247945486391385249259848502175234010967289831554894776077704571261457595823825245669052206379832284446373088109050246642453540203667448240894956074979263603360448779126929364191229791046048600648158120404404766763070327940029813826415327745664993191485439444296109763969948631755535163926384703087422857642736153852582820056661551903549876616627900530084158172809851351898663554970528201875223815554349604138636668040631,
        28796899277235049975421947378568428888005019408631005870725337759187744546493409470582705210790627097597656481534493716225301660663533212040068163723937803169735485217437722947354732420098585958967033073629288721874028940705969141716032409906092583043329293532612601200186754187377338924379443611709918885185638934712580040042904995838353611699081350712817357237035507539201368300463060034856220488010509411264244138417348439340955309300128758040513940379009974696105387107481999359705587790254117489020540714253505694682552102843028243384677060490696214834957049391213864664165843655260698241682369402177091178720927,
        28349223152666012309896421767725787316124897111416473420803849019741154117582482568645254183215552986563114855665416593397403745371086355268654763921803558654340155902194948080056226592560917521612824589013349044205989541259468856602228462903448721105774109966325479530181197156476502473067978072053273437369680433495259118953717909524799086692640103084287064091489681162498108275295255082627807077949841602061428289272700263987438087045434043977981316071156426134695316796020506076336851840708593720052204359360366058549157961154869248835793804817253083037277453771408544063058190126149127240681909811943783388977967,
        28349223152666012309896421767725787316124897111416473420803849019741154117582482568645254183215552986563114855665416593397403745371086355268654763921803558654340155902194948080056226592560917521612824589013349044205989541259468856602228462903448721105774109966325479530181197156476502473067978072053273437369680433495259118953717909524799086692640103084287064091489681162498101607280822202773532998098050880803631144514377948079277690787622279940743498439084904702494445241729763146426258407468147831250550239995285695193105630324823153678214290802694619958991541957383815098042054239547145549933872335482492225099839,
        2758599203,
        199050626189790903113151725251371951406311367304411013359159100762029303668345459282823483508119186508070350039475140948570888009866572148405365532164833126992414461936781273087675274788769905198546175946505790118332257676994622928414648644875376193656132263418075334807302665038501361680530751104620475935886499714767992159620130246904875540624651891646715835632182355428589610236128648209568297096024509697960196858754170641081387466229916585122877955908862176165344465889280850859817985096316883025515924332365977538735425288433292357532172467247159245727072344354499113900733623716569924461327947462469348798798400461045817375922057805611166274339541877392159201774893120311667898551312256530117094221191204981071357303328506659872809131929265966688409379037586014938643190675726674943253875287765020503118408406103824607730713529079962656130622218633922911733000466212212532871890933508287965723844399784165195088175666883742686183165151553009638524764735387233844317375317153437534933611361683136151569588355535831475925641431859231311079029505004457816932257031352498323214304125608733640306746900473758755832661915903475867854937735150255829715879232213599597863424779218670961633567259935246911742292942052832671549,
        24333562944687516822197571192658754203291290861678417217447438854540594847087766562404339574537862439116548079253289466115128767870577648533973566286797593441730003379848043825634065823911136780045362090360846493427099473619203426216220826743478974241107765471416754913629766068614128278553165309459614540881272639715963742807416312087758332567870818068056326342400589601117982695439948496482753836668023789721452705706258642830333890588979897355741176673670662543132574318628603066958811749579934075668455748590286427527491514861437629540690813171672435522560204943058263324060332232490301430308879676240097644556943,
        25699922293123622238012005113928758274338093880738911843144609876290300384447243164527369410936522534026502861166228851341858617366580840945546916656960397913459416157594030359887797479829819533476376181670391998963549074371737295746623468123112547424135047636878302121269250886314724602949616886176008642837449632045010113812032294774060357611189602487961064611234002464905006798590256478016955856378120527444702590839053848988168714049387256070864726124290373739801554166928887083826045058481026363141572007235867367607974662051368481037707609970666363610931674810380477197023311110704572295255843715262143691203301,
        26641239846781539174997613915486416003684568556746576609279663468469031683562139918289710191916575980269872103186803161203776420494840845869372424906386190919487401478921545410628828040240934885968480468559124463233908052442280478139872489261920279274813374296134128578293855845928227225795788061940296913771355415137193729864318300987109915105382195425114525826138321815629366884757211418011082865207792823895128910178064295532964692290697547400111032047363746813247658976480566291220338236760240639947583180060309174234225896967104503916386813098322083010876516252218060276731781117933746509243898480864478441202823,
        136417036410264428599995771571898945930186573023163480671956484856375945728848790966971207515506078266840020356163911542099310863126768355608704677724047001480085295885211298435966986319962418547256435839380570361886915753122740558506761054514911316828252552919954185397609637064869903969124281568548845615791,
        11232077261967644077277312997808249915855709514498625183789998098688209996914964867050110603375257386497746294969159136128904120786273278056895662599793297,
    ]
    for prime in primes:
        if publickey.n % prime == 0:
            publickey.q = prime
            publickey.p = publickey.n // publickey.q
            priv_key = PrivateKey(
                int(publickey.p), int(publickey.q), int(publickey.e), int(publickey.n)
            )
            return (priv_key, None)
    return (None, None)
