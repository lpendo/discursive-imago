import streamlit as st

ArcanuaTup = (
    "Death", "Fate", "Forces", "Life", "Matter", "Mind", "Prime", "Space", 
    "Spirit", "Time"
)

HighArc = st.selectbox(
    "What is the highest Arcanum used in the spell?",
    ArcanuaTup,
    index=None,
    placeholder="Arcanum?" 
)

RankTup = ("●Initiate", "●●Apprentice", "●●●Disciple", 
     "●●●●Adept", "●●●●●Master")

RitualIntervalTup = (
    "3 Hours","1 Hour", "30 Minutes", "10 Minutes", "1 Minute"
)

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

    CasterGnosis = st.selectbox(
        "What is the caster's level of Gnosis?",
        range(1,11),
        placeholder="Gnosis?"
    )

    GnosisIdx = (CasterGnosis-1) // 2

    RitualInterval = RitualIntervalTup[GnosisIdx]

    HighArcDots = 5
    if HighArcStr != None: HighArcDots = RankTup.index(HighArcStr) 

    CasterArcDots = 0
    if CasterArcStr != None: CasterArcDots = RankTup.index(CasterArcStr)

    FreeReach = CasterArcDots - HighArcDots + 1

    if FreeReach > 0:

        CastingType = st.selectbox(
            "What is the spellcasting method?",
            ("Improvised","Rote","Praxis"),
            index=0
        )

        if CastingType == "Rote": FreeReach = 5 - HighArcDots + 1
        st.write("Free Reach:", FreeReach)

        Reach = 0

        CastingType = st.selectbox(
            "What is the Primary Spell Factor?",
            ("Potentcy","Duration"),
            index=0
        )

        # CastingPotency = 

        CastingTime = st.selectbox(
            "What is the spellcasting duration?",
            ("Ritual ("+RitualInterval+")","Instant",),
            index=0
        )
        if CastingTime == "Instant": Reach += 1

        CastingRange = st.selectbox(
            "What is the spellcasting range?",
            ("Self/Touch","Sensory",),
            index = 0
        )
        if CastingRange == "Sensory": Reach += 1

        st.write("Total Reach used in Spell:", Reach)
        ParadoxReach = max(0,Reach-FreeReach)
        st.write("Total Paradox Reach:", ParadoxReach)

        

    else:
        st.write("Spell cannot be cast!")

# Mana = 0
# Reach = 0
# Potency = 1

# EffectsL = ( "Inflict Damage", "Perform Healing", "Impose a Condition/Tilt",
#             "Provide a Bonus/Penalty to a Trait", "Add a dice poll efffect", 
#             "Protect something", "Hide something" )
# Effects = st.selectbox("What is your spell going to do?",EffectsL)

# PracticesL = (
#     ( "●Compelling", "●Knowing", "●Unvieling", ),
#     ( "●●Ruling", "●●Shielding", "●●Veiling", ),
#     ( "●●●Fraying", "●●●Perfecting", "●●●Weaving", ),
#     ("●●●●Patterning", "●●●●Unraveling", ),
#     ("●●●●●Making", "●●●●●Unmaking" ),
# )
# # Practice = st.selectbox("Which practice?",PracticesL)


# # RankL = ( "Initiate(●)", "Apprentice(●●)", "Disciple(●●●)", "Adept(●●●●)",
# #          "Master(●●●●●)" )
# # Rank = st.selectbox("What rank?",RankL)


# # st.write("Path:", MagePath)
# # st.write("Arcana:", Arcana)

# if Effects == EffectsL[0]:
#     DamageKind = ("Bashing", "Lethal", "Aggravated")
#     DamageType = st.selectbox("Damage type?", DamageKind)

#     if DamageType == DamageKind[0]:
#         Practice = PracticesL[2][0]
#     else:
#         Practice = PracticesL[3][1]
        
#     if DamageType == DamageKind[2]:
#         Mana += 1
#         Reach += 1

#     DamageAmount = st.selectbox("How much damage?", )

# if Effects == EffectsL[1]:
#     DamageKind = ("Bashing", "Lethal", "Aggravated")
#     DamageType = st.selectbox("Damage type?", DamageKind)

#     if DamageType == DamageKind[0]:
#         Practice = PracticesL[2][0]
#     if DamageType == DamageKind[1]:
#         Practice = PracticesL[3][1]
#     if DamageType == DamageKind[2]:
#         Practice = PracticesL[4][1]



# st.write("Effect:", Effects)
# st.write("Effect:", Practice)