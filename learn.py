import streamlit as st

MagePath = st.selectbox(
    "What is your Path?",
    ("Acanthus", "Moros", "Mastigos", "Obrimos", "Thyrsus"),
    placeholder="Path?"
)


Arcana = st.selectbox(
    "Arcana of spell?",
    ("Death", "Fate", "Forces", "Life", "Matter", "Mind", "Prime",
     "Space", "Spirit", "Time"),
    placeholder="Arcana?" 
)

Effects = st.selectbox(
    "What is your spell going to do?",
    ("Inflict Damage", "Perform Healing", "Impose a Condition/Tilt", 
     "Provide a Bonus/Penalty to a Trait", "Add a dice poll efffect",
     "Protect something", "Hide something"),
)

Practices = st.selectbox(
    "Which practice?",
    ( "●Compelling", "●Knowing", "●Unvieling",
     "●●Ruling", "●●Shielding", "●●Veiling",
     "●●●Fraying", "●●●Perfecting", "●●●Weaving",
     "●●●●Patterning", "●●●●Unraveling",
     "●●●●●Making", "●●●●●Unmaking",
      )
)




st.write("Path:", MagePath)
st.write("Arcana:", Arcana)