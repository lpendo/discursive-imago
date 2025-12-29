import streamlit as st

sesh = st.session_state

ArcanumTup = (
    "Death", "Fate", "Forces", "Life", "Matter", "Mind", "Prime", "Space", 
    "Spirit", "Time"
)


RankTup = ("●Initiate", "●●Apprentice", "●●●Disciple", 
    "●●●●Adept", "●●●●●Master")


RitualIntervalTup = (
    "3 Hours", "1 Hour", "30 Minutes", "10 Minutes", "1 Minute"
)


StandDurationTup = (
    "1 turn", "2 turn", "3 turns", "5 turns", "10 turns", ">10 turns"
)
AdvDurationTup = (
    "1 hour", "1 day", "1 week", "1 month", "1 year", "Indefinite*"
)


StandDurationTup = (
    "1 turn", "2 turn", "3 turns", "5 turns", "10 turns", ">10 turns"
)
AdvDurationTup = (
    "1 hour", "1 day", "1 week", "1 month", "1 year", "Indefinite*"
)


StandSubjectNumTup = (
    "1 subject of up to Size 5", "2 subjects of up to Size 6", 
    "4 subjects of up to Size 7", "8 subjects of up to Size 8",
    "16 subjects of up to Size 9",
)




AdvSubjectNumTup = (
    "5 subjects up to Size 5", "10 subjects up to Size 10",
    "20 subjects up to Size 15", "40 subjects up to Size 20",
    "80 subjects up to Size 25", "160 subjects up to Size 30"
)


StandAreaTup = (
    "Arm's reach from a central point", "A small room", 
    "A large room", "Several rooms, or a single floor", 
    "A ballroom or small house",
)

AdvAreaTup = (
    "Large building", "A small warehouse or parking lot", 
    "A large warehouse or supermarket", 
    "A small factory or a shopping mall", 
    "A ballroom or small house",
) 


SimpleYantrasTup = (
    ("Demesne/Verge", 2,), ("Resonant Environment", 1),
    (
        "Concentration (requires Duration longer than a turn,"
        +" must be maintained)", 
        2
    ),
    ("Mantra (requires High Speech Merit)", 2),
    ("Runes", 2), ("Path/Order/Dedicated Tool", 1),
    ("Material sympathy", 2), ("Representational sympathy", 1),
    ("Common material Sacrament", 1),
    ("Special material Sacrament", 2),
    ("Non-material Sacrament", 3),
)

PrereqTantrasTup = (
    ("Mudra/Rote", "Skill Dots?",),
    ("Exarch Prelacy", "Prelacy Dots?",),
    ("Persona", ("Shadow Name Dots?", "Cabal Theme Dots?"),),
)
#-------------------------------------------------------------------------------

def ResetYantras():
    sesh.YantraIdxs = [False] * len(SimpleYantrasTup)
    for n in range(len(sesh.YantraIdxs)):
        sesh["SimpleYantra"+str(n)] = sesh.YantraIdxs[n]



#-------------------------------------------------------------------------------
HighArc = st.selectbox(
    "What is the highest Arcanum used in the spell?",
    ArcanumTup,
    index=None,
    placeholder="Arcanum?" 
)
RulingArcana = st.checkbox("Is this a Ruling Arcana for your Path?")


st.divider()

if HighArc != None:
    HighArcStr = st.selectbox(
        "What number of dots in "+HighArc+" is required for the spell?",
        RankTup,
        index=None,
        placeholder="No. of Dots?" 
    )

    CasterArcStr = st.selectbox(
        "What number of dots does the caster have in "+HighArc+"?",
        RankTup,
        index=None,
        placeholder="No. of Dots?" 
    )



    st.divider()

    HighArcDots = 5
    if HighArcStr != None: HighArcDots = RankTup.index(HighArcStr) + 1

    CasterArcDots = 0
    if CasterArcStr != None: CasterArcDots = RankTup.index(CasterArcStr) + 1

    FreeReach = CasterArcDots - HighArcDots + 1

    WithstandRating = CasterArcDots

    if FreeReach > 0:

        CasterGnosis = st.selectbox(
            "What is the caster's level of Gnosis?",
            range(1,11),
            index=None,
            placeholder="Gnosis?",
            on_change=ResetYantras
        )
        
        if CasterGnosis:

            GnosisIdx = (CasterGnosis-1) // 2
            sesh.NumberOfYantras = GnosisIdx + 2
            sesh.BaseRitualInterval = RitualIntervalTup[GnosisIdx]
            sesh.RitualCastingText = (
                "Ritual ("
                + sesh.BaseRitualInterval
                + ")"
            )
            sesh.ParadoxPerReach = GnosisIdx+1


            st.divider()

            CastingType = st.selectbox(
                "What is the spellcasting method?",
                ("Improvised","Rote","Praxis"),
                index=0
            )
            if not RulingArcana and CastingType == "Improvised":
                Mana = 1
            else:
                Mana = 0


            st.divider()

            if CastingType == "Rote": FreeReach = 5 - HighArcDots + 1
            st.write("Free Reach:", FreeReach)



            st.divider()

            Reach = 0
            SpellFactorPenalty = 0

            if st.checkbox(
                "Spend a Reach for +2 to Withstand dispellation?", 
                value=False
            ):
                Reach += 1
                WithstandRating += 2



            st.divider()

            if st.checkbox(
                "Spend a Reach to change the Primary Spell Factor?", 
                value=False
            ):
                Reach += 1

            CastingType = st.selectbox(
                "What is the final Primary Spell Factor?",
                ("Potency","Duration"),
                index=0
            )

            MinPotency = 1
            MinDuration = 0
            MinFactor = CasterArcDots - 1
            if CastingType == "Potency": MinPotency += MinFactor
            if CastingType == "Duration": MinDuration += MinFactor
            
            
            st.divider()

            CastingRange = st.selectbox(
                "What is the spellcasting range?",
                ("Self/Touch","Sensory",),
                index = 0
            )
            if CastingRange == "Sensory": Reach += 1

            
            
            st.divider()
            
            SpellPotency = st.number_input(
                "Set the Potency of the Spell",
                min_value=MinPotency,
                max_value=30
            )
            SpellFactorPenalty += -2*( SpellPotency - MinPotency )
            # st.write("MinPotency: ", MinPotency)
            
            st.divider()

            # MinDurationIdx = 0
            # if CastingType == "Duration": MinDurationIdx += CasterArcDots - 1
            
            AdvDur = st.checkbox(
                "Spend a Reach for Advanced Duration?", value=False
            )

            if AdvDur:
                DurationTup = AdvDurationTup[MinDuration:]
                Reach += 1
            else:
                DurationTup = StandDurationTup[MinDuration:]

            SpellDuration = st.selectbox(
                "Set the Duration Spell Factor of your spell?",
                DurationTup,
                index = 0
            )

            if SpellDuration == DurationTup[-1] and not AdvDur:
                SpellDurationVal = st.number_input(
                    "Set the duration of the Spell (in turns)",
                    min_value=11,
                    max_value=159
                )
                SpellFactorPenalty += -2*( ( SpellDurationVal - 10 )//10 )

            if SpellDuration == AdvDurationTup[-1]:
                IndefiniteSpell = st.checkbox(
                    "Will you spend a Reach and a Mana to make the spell "
                    + "have Indefinite duration?",
                    value = True
                )
                if IndefiniteSpell:
                    Reach += 1
                    Mana += 1
                else:
                    st.write(
                        "Without spending a Reach and a Mana, ",
                        "Spell Duration is limited to 1 year."
                    )
                    SpellDuration = AdvDurationTup[-2]

            SpellFactorPenalty += -2*( DurationTup.index(SpellDuration) )


            st.divider()

            AdvScale = st.checkbox(
                "Spend a Reach for Advanced Scale?", value=False
            )

            ScaleType = st.selectbox(
                "What type of Scale are you using?",
                ("Number of Subjects","Area of Effect",),
                index = None,
                placeholder="Type?" 
            )

            if ScaleType is None:
                st.stop()
            else:
                if AdvScale:
                    if ScaleType == "Number of Subjects":
                        ScaleTup = AdvSubjectNumTup
                    else:
                        ScaleTup = AdvAreaTup
                else:
                    if ScaleType == "Number of Subjects":
                        ScaleTup = StandSubjectNumTup
                    else:
                        ScaleTup = StandAreaTup

                SpellScale = st.selectbox(
                    "Set the Scale Spell Factor of your spell?",
                    ScaleTup,
                    index = 0
                )

                ScaleIdx = ScaleTup.index(SpellScale)
                SpellFactorPenalty += -2*ScaleIdx


            st.divider()

            CastingTimeBonus = 0
            CastingTime = st.selectbox(
                "What is the spell casting time?",
                (sesh.RitualCastingText,"Instant",),
                index=0
            )
            if CastingTime == "Instant": 
                Reach += 1
            else:
                RitualIntervals = st.number_input(
                    "How many Ritual spellcasting intervals will you use?",
                    min_value=1,
                    max_value=6
                )
                CastingTimeBonus = RitualIntervals-1
            
                num,unit = sesh.BaseRitualInterval.split()
                num = int(num) * RitualIntervals
                if unit == "Minutes":
                    if num >= 60:
                        num /= 60
                        unit = "Hours"
                st.write("Total spellcasting time:", str(num)+" "+unit)
                st.write("Total spellcasting time Bonus:", CastingTimeBonus)

            st.divider()

            st.write("Yantras?")
            st.write(
                "You are limited to "
                ,str(sesh.NumberOfYantras)
                ," Yantras total."
                ," This is determine by your Gnosis."
            )

            YantraBonus = 0
            for n in range(len(sesh.YantraIdxs)):
                if "SimpleYantra"+str(n) not in sesh:
                    sesh["SimpleYantra"+str(n)] = False
                sesh.YantraIdxs[n] = sesh["SimpleYantra"+str(n)]


            sesh.YantrasLeft = sesh.NumberOfYantras - sum(sesh.YantraIdxs)
            if sesh.YantrasLeft == 0:
                st.write("No Yantras left!")
            else:
                st.write("You have "+str(sesh.YantrasLeft)+" Yantras left.")

            for idx,(type,val,) in enumerate(SimpleYantrasTup):
                YTxt = type+" (+"+str(val)+")"
                YKey = "SimpleYantra"+str(idx)
                if sesh.YantrasLeft == 0:
                    if sesh.YantraIdxs[idx]:
                        st.checkbox(YTxt,key=YKey)
                        YantraBonus += val
                else:
                    st.checkbox(YTxt,key=YKey)
                    if sesh.YantraIdxs[idx]:
                        YantraBonus += val
                        
            st.write("Yantra Bonus:", YantraBonus)


            st.divider()
            
            MiscBonus = st.number_input(
                    "Any other bonuses?",
                    min_value=0,
                    max_value=40
            )

            MiscPenalty = st.number_input(
                    "Any other penalties?",
                    min_value=0,
                    max_value=40
                )


            st.divider()
            DicePool = CasterGnosis+CasterArcDots
            st.write("Initial spellcasting Dice Pool:", DicePool)
            
            
            st.divider()
            st.write("Spellcasting Factors Penalty:", SpellFactorPenalty)
            st.write("Raw Yantra Bonus:", YantraBonus)
            
            SpellAdj = max(5,YantraBonus+SpellFactorPenalty)
            st.write(
                "Yantra Bonus after mitigating Spell Factors (max +5):"
                ,SpellAdj
            )


            st.divider()
            st.write("Casting Time Bonus:", CastingTimeBonus)
            st.write("Other Bonus:", MiscBonus)
            st.write("Other Penalty:", -abs(MiscPenalty))

            DicePool += CastingTimeBonus+MiscBonus - abs(MiscPenalty)
            st.write(
                "Final Dice Pool (before penalties from released Paradox):", 
                DicePool
            )


            st.divider()
            st.write("Mana?")

            Mana += st.number_input(
                "How much Mana does the spell require?",
                min_value=0,
                max_value=100
            )

            ParadoxMana =st.number_input(
                "Will you use any Mana to counteract Paradox?",
                min_value=0,
                max_value=100
            )
            Mana += ParadoxMana

            st.write("Total Mana required to cast the spell:", Mana)


            st.divider()
            st.write("Paradox?")

            # st.write("Total Reach used in Spell:", Reach)
            ParadoxReach = max(0,Reach-FreeReach)
            ParadoxDice = sesh.ParadoxPerReach*ParadoxReach
            st.write("Total Paradox Dice from Reach:", ParadoxDice)
            
            if st.checkbox("Are you inured to the spell?"):
                ParadoxDice += 2

            if st.checkbox("Did any Sleepers witness an obvious casting of magic?"):
                ParadoxDice += 1
                SleeperDiceQuality = st.selectbox(
                    "How many Sleepers saw your casting?",
                    (
                        "One",
                        "A few",
                        "A lot, less than 100",
                        "More than a hundred", 
                    )
                )
            if st.checkbox("Are you using a dedicated magical tool?"):
                ParadoxDice -= 2

            ParadoxDice -= ParadoxMana
            st.write("Total Paradox Dice after Mana amelioration:", ParadoxDice)

            ParadoxChoice = st.selectbox(
                "Do you wish to Release or Contain Paradox?",
                ("Release","Contain"),
                index=0
            )

        # else:
        #     st.write("Please set your Gnosis!")
        

    else:
        st.write("Spell cannot be cast!")