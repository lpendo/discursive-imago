import streamlit as st

ArcanumTup = (
    "Death", "Fate", "Forces", "Life", "Matter", "Mind", "Prime", "Space", 
    "Spirit", "Time"
)


RankTup = ("●Initiate", "●●Apprentice", "●●●Disciple", 
     "●●●●Adept", "●●●●●Master")


RitualIntervalTup = (
    "3 Hours","1 Hour", "30 Minutes", "10 Minutes", "1 Minute"
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


YantrasTup = (
    ("Demesne/Verge", 2,), ("Resonant Environment", 1),
    ("Concentration (requires Duration longer than a turn)", 2),
    ("Mantra (requires High Speech Merit)", 2),
    ("Runes", 2), ("Path/Order/Dedicated Tool", 1),
    ("Material sympathy", 2), ("Representational sympathy", 1),
    ("Common material Sacrament", 1),
    ("Special material Sacrament", 2),
    ("Non-material Sacrament", 3),
    ("Mudra/Rote", "Skill Dots?",),
    ("Exarch Prelacy", "Prelacy Dots?",),
    ("Persona", ("Shadow Name Dots?", "Cabal Theme Dots?"),),
)

#-------------------------------------------------------------------------------
HighArc = st.selectbox(
    "What is the highest Arcanum used in the spell?",
    ArcanumTup,
    index=None,
    placeholder="Arcanum?" 
)



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
            placeholder="Gnosis?"
        )
        GnosisIdx = (CasterGnosis-1) // 2
        RitualInterval = RitualIntervalTup[GnosisIdx]



        st.divider()

        CastingType = st.selectbox(
            "What is the spellcasting method?",
            ("Improvised","Rote","Praxis"),
            index=0
        )

        st.divider()

        if CastingType == "Rote": FreeReach = 5 - HighArcDots + 1
        st.write("Free Reach:", FreeReach)



        st.divider()

        Reach = 0
        Mana = 0
        DicePenalty = 0

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

        st.write("Potency Min: ", MinPotency)
        st.write("Duration Min Idx: ", MinDuration)

        st.divider()

        CastingTime = st.selectbox(
            "What is the spell casting time?",
            ("Ritual ("+RitualInterval+")","Instant",),
            index=0
        )
        if CastingTime == "Instant": Reach += 1

        
        
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
            min_value=MinPotency
        )
        DicePenalty += -2*( SpellPotency - MinPotency )
        st.write("MinPotency: ", MinPotency)
        
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
                "Set the duration of the Spell",
                min_value=11
            )
            DicePenalty += -2*( ( SpellDurationVal - 10 )//10 )

        if SpellDuration == AdvDurationTup[-1]:
            if st.checkbox(
                "Will you spend a Reach and a Mana to make the spell have Indefinite duration?",
                value = True
            ):
                Reach += 1
                Mana += 1
            else:
                st.write("Without spending a Reach and a Mana, Spell Duration is limited to 1 year.")
                SpellDuration = AdvDurationTup[-2]

        DicePenalty += -2*( DurationTup.index(SpellDuration) )



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

        if ScaleType != None:
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
            DicePenalty += -2*ScaleIdx


        st.divider()

        st.write("Yantras?")

        st.checkbox(YantrasTup[0][0])



        st.divider()

        st.write("Final Dice Penalty to spellcasting:", DicePenalty)

        st.write("Total Reach used in Spell:", Reach)
        ParadoxReach = max(0,Reach-FreeReach)
        st.write("Total Paradox Reach:", ParadoxReach)

        

    else:
        st.write("Spell cannot be cast!")