# Suggested Edits -- Tales of Argosa MD

Source-level issues found while transcribing *Tales of Argosa* (Tales_of_Argosa_5_4_25_reduced.pdf). **None of these has been applied**: every note keeps the book's text exactly as printed. Tick an item once you've decided (fix it in the vault, or keep it as printed).

- Compiled 2026-11-25 from the batch reports (A1-A10, C1-C14), the table image check (T01-T12), the prose triage (R1, R2) and the linking reports (L1-L7). An issue reported by several agents is listed once.
- Pages are given as PDF page / printed page (printed = PDF - 2).
- Quotes are the printed words. Bold/italic markers are left out unless the emphasis itself is the issue.
- Where a quote has since been wrapped in a link, the displayed words are unchanged. A dropped page reference is noted.

## Book-wide (recurring)

- [ ] "Sever Arcarnum": the spell name is printed this way 11 times, including its own heading (PDF 110 / p.108). Likely "Sever Arcanum". Because the book is consistent, it may be the author's own spelling. To change it you would rename `15. Sorcery/15.9. Spells/Sever Arcarnum.md` and its links. It appears in:
  - "Sever Arcarnum" -- `5. Classes/5.5.2. Spell Like Blessings.md` -- PDF 27 / p.25
  - "Sever Arcarnum" -- `15. Sorcery/15.8.1. Spell List.md` -- PDF 103 / p.101
  - "Sever Arcarnum" -- `15. Sorcery/15.9. Spells/Flesh to Stone.md` -- PDF 107 / p.105
  - "Sever Arcarnum" -- `15. Sorcery/15.9. Spells/Sever Arcarnum.md` (filename; heading on PDF 110 / p.108)
  - "Sever Arcarnum" -- `16. Downtime/16.7. Potion Brewing_.md` (Special Ingredient table) -- PDF 125 / p.123
  - "Sever Arcarnum" -- `21. Monsters/21.4. Bestiary/Shade.md` -- PDF 200 / p.198
  - "Sever Arcarnum" -- `24. Rival Adventurers/24.1. Rival Adventurers_.md` -- PDF 216-217 / p.214-215
  - "Sever Arcarnum" -- `26. Traps/26.4.2. Triggers & Counters.md` -- PDF 225 / p.223
  - "Sever Arcarnum" -- `27. Treasure/27.5.2. Potions.md` -- PDF 242 / p.240
  - "Sever Arcarnum" -- `27. Treasure/27.6. Old Magic Grimoires/Reaper of Hidden Shadow.md` -- PDF 244 / p.242
- [ ] "henchmen" used for the singular, where "henchman" is likely meant:
  - "Earn a new henchmen." -- `16. Downtime/16.2. Advancement_.md` (Social xp table) -- PDF 117 / p.115
  - "A random NPC (hireling, henchmen, other NPC)" -- `17. GM Tools/17.4.4. Travel Events.md` (row 17) -- PDF 140 / p.138
  - "If a PC declines a henchmen, or if the henchmen has any outstanding Payback" -- `18. Hirelings/18.6. Hireling Advancement_.md` -- PDF 161 / p.159
  - "Transforms into a beautiful henchmen." -- `18. Hirelings/18.6.1. Hireling Advancement.md` (row 11-12) -- PDF 161 / p.159
  - "a free random henchmen for one year" -- `20. Mass Battle/20.1.1. Field Events.md` (row 8) -- PDF 164 / p.162
  - "A hireling, henchmen, pet" -- `20. Mass Battle/20.2.1. Sudden Twist.md` (row 4) -- PDF 166 / p.164
- [ ] Other "-man / -men" mix-ups:
  - "a brave woodsmen" (woodsman) -- `5. Classes/5.9. Ranger_.md` -- PDF 40 / p.38
  - "a stray crossbow bolt or distant marksmen takes" (marksman) -- `20. Mass Battle/20.2.1. Sudden Twist.md` (row 1) -- PDF 166 / p.164
  - "a mix of guardsman and hunched, cowled figures" (guardsmen) -- `17. GM Tools/17.5.2. City, Town, Village.md` -- PDF 144 / p.142
- [ ] "statute" where "statue" is meant:
  - "unearthed a humanoid statute with a beetle like head" -- `17. GM Tools/17.5.3. Deserts.md` (row 7) -- PDF 146 / p.144
  - "A 15 ft stone statute,in the likeness of a serpentman" -- `17. GM Tools/17.5.4. Jungles.md` (row 4) -- PDF 147 / p.145 (there is also no space after the comma)
- [ ] "puss" where "pus" is meant:
  - "causing nails to emit yellow puss" -- `17. GM Tools/17.5.4. Jungles.md` (row 2) -- PDF 147 / p.145
  - "I survived the puss puddle plague." -- `18. Hirelings/18.5.2. Catchphrase.md` (row 69-70) -- PDF 161 / p.159 (may be deliberate slang)
- [ ] "outnumber foe" -- likely "when outnumbering a foe":
  - "extra +1 to attack when outnumber foe" -- `5. Classes/5.9. Ranger_.md` (Wolf beast companion) -- PDF 41 / p.39
  - "extra +1 to attack when outnumber foe" -- `21. Monsters/21.4. Bestiary/Wolf (or Dog).md` -- PDF 174 / p.172
  - "when outnumber foe" -- `21. Monsters/21.4. Bestiary/Raptor.md` -- PDF 180 / p.178
- [ ] "Adaption" where "Adaptation" is likely meant:
  - "INJURY ADAPTION" (heading; it is the filename) -- `7. Unique Features/7.2. Example Unique Features/Injury Adaption.md` -- PDF 49 / p.47
  - "adaption training" -- `16. Downtime/16.8. Recovery_.md` -- PDF 126 / p.124
- [ ] Monster names spelled differently in different places. These mismatches also kept the links from forming:
  - "Serpentman (Hraarsk)" vs the heading HRAASK -- `21. Monsters/21.2.1. Monsters by HD.md` (PDF 169 / p.167). The Hraask entry spells it "Hraarsk" in its own text: `21. Monsters/21.4. Bestiary/Hraask.md` and `21. Monsters/21.4. Bestiary/Serpentmen.md` (PDF 199 / p.197), and so do `17. GM Tools/17.5.4. Jungles.md` (PDF 147) and `17. GM Tools/17.5.11. Swamps.md` (PDF 156). Pick one spelling.
  - "Serpentman (Ssurlock)" vs the heading SSURLOC -- `21. Monsters/21.2.1. Monsters by HD.md` -- PDF 169 / p.167
  - "Wing Snake" vs the heading WINGED SNAKE -- `21. Monsters/21.2.1. Monsters by HD.md` -- PDF 169 / p.167
  - "Hell Hound" vs the heading DEMON, HELLHOUND -- `21. Monsters/21.2.1. Monsters by HD.md` (PDF 169), `15. Sorcery/15.9. Spells/Conjure Entity.md` (PDF 106), `16. Downtime/16.7. Potion Brewing_.md` (PDF 125), `16. Downtime/16.11. Scroll Inscribing_.md` (PDF 128)
  - "Spider (Giant, Nestmother)" vs the stat block NEST MOTHER -- `21. Monsters/21.2.1. Monsters by HD.md` -- PDF 169 / p.167
  - "N'tarc" / "N'Tarc" in the text vs the heading N'TARC -- `21. Monsters/21.4. Bestiary/N'Tarc.md` -- PDF 194-195 / p.192-193
  - "Monster by HD chart" vs the table title MONSTERS BY HD -- `17. GM Tools/17.5. Encounter Tables_.md` (PDF 142), `25. Solo Rules/25.4. Dungeon Generator_.md` (PDF 221)
  - Monsters by HD also lists "Dog" separately (dogs use the Wolf entry), and lists a plain "Elemental" at both HD 5 and HD 9-10 -- `21. Monsters/21.2.1. Monsters by HD.md` -- PDF 169 / p.167
- [ ] US spellings in a book that otherwise uses UK spelling:
  - "Traveling" -- `5. Classes/5.9. Ranger_.md` (Rangercraft intro, PDF 41 / p.39) and `11. Encounters/11.2.1. Activity.md` (row 5, PDF 68 / p.66)
  - "Specialized" -- `8. Skills & Rerolls/8.1. Skills_.md` (Skills table, PDF 55 / p.53) and "specialized" -- `17. GM Tools/17.5.2. City, Town, Village.md` (PDF 143 / p.141)
- [ ] "referee's" where the book otherwise says "GM's" (probably harmless, flagged for consistency):
  - "(referee's call)" -- `15. Sorcery/15.9. Spells/Whispers of the Watchers.md` -- PDF 112 / p.110
  - "the referee's control" -- `21. Monsters/21.3. Special Traits_.md` -- PDF 172 / p.170
  - "(referee's call)" -- `21. Monsters/21.4. Bestiary/Vampire.md` -- PDF 205 / p.203
  - "At the referee's discretion" -- `27. Treasure/27.6. Old Magic Grimoires/Rite of Revelation.md` -- PDF 244 / p.242

## 1. What Is Tales of Argosa

- [ ] "pain... <the GM rolls a Dex check, which fails> .., and he topples" -- `1. What Is Tales of Argosa/1.3. How to Play_.md` -- PDF 8 / p.6. Stray "..". Likely "..." or nothing.
- [ ] "ten-sided" vs "six sided", "twelve sided" in the same sentence -- `1. What Is Tales of Argosa/1.3. How to Play_.md` -- PDF 9 / p.7. Hyphenation is inconsistent (low priority).

## 2. Character Creation

- [ ] "Persuasion. Pipe, Drum, Horn, or Lute" -- `2. Character Creation/2.1.1. Backgrounds.md` (row 61 Busker) -- PDF 11 / p.9. A full stop where every other row has a comma.

## 4. Races

- [ ] "Halfling" heading is singular where the other race headings are plural -- `4. Races/4.1. Races_.md` -- PDF 16 / p.14. Likely "Halflings".

## 5. Classes

- [ ] Missing commas in the class skill lists. Likely "..., (x) ..." throughout:
  - "(ix) Watercraft (x) Sleight of Hand" -- `5. Classes/5.2. Artificer_.md` -- PDF 18 / p.16
  - "(viii) Stealth (ix) Watercraft" -- `5. Classes/5.4. Bard_.md` -- PDF 24 / p.22
  - "(vii) General Lore (viii) Persuasion, (ix) Watercraft (x) Stealth" -- `5. Classes/5.6. Fighter_.md` -- PDF 32 / p.30
  - "(ii) Deception (iii)", "(vi) General Lore (vii)", "(viii) Watercraft (ix)" -- `5. Classes/5.7. Magic User_.md` -- PDF 35 / p.33
  - "(ix) Watercraft (x)" -- `5. Classes/5.9. Ranger_.md` -- PDF 40 / p.38
- [ ] "Five deities from the Argosa Sandbox are provided below" -- `5. Classes/5.5. Cultist_.md` -- PDF 28 / p.26. Six gods follow (Argona, Baal, Graxus, Shennog, Soliri, Wodon). Likely "Six".
- [ ] "Add the following to Spell like Blessing:" -- `5. Classes/5.5. Example Gods/Baal (Lord of Crows).md` -- PDF 29 / p.27. Singular, where the other gods say "Blessings".
- [ ] "Backstab Boost" at Level 5 in the Rogue table has no heading of its own -- `5. Classes/5.10. Rogue_.md` -- PDF 43 / p.41. It is the 5th-level line inside Backstab. Possibly the table should say "Backstab" (low priority).

## 7. Unique Features

- [ ] "an Int (Perception) check" -- `7. Unique Features/7.2. Example Unique Features/Born to Loot.md` (tier 2) -- PDF 48 / p.46. Perception is an attribute, not a skill. Likely "Perc (Detection)" or "Int (Detection)".
- [ ] "MONK TECHNIQUES (CROSS CLASS)" (heading; it is the filename) vs "(CROSSCLASS)" on every other crossclass feature -- `7. Unique Features/7.2. Example Unique Features/Monk Techniques (Cross Class).md` -- PDF 49 / p.47.

## 8. Skills & Rerolls

- [ ] "only one of the results are rerolled" -- `8. Skills & Rerolls/8.2. Rerolls_.md` -- PDF 54 / p.52. Likely "is rerolled".
- [ ] "identify weak points on rooftop" -- `8. Skills & Rerolls/8.2. Rerolls_.md` (Backgrounds paragraph) -- PDF 54 / p.52. Likely "on a rooftop" or "on rooftops".

## 9. Equipment

- [ ] "44 Pickaxe" and "44 Pole, 10 ft" -- `9. Equipment/9.3.1. Common Gear.md` -- PDF 58 / p.56. 44 is printed twice and 45 is missing. Likely "45 Pole, 10 ft".
- [ ] "available in most villages ." -- `9. Equipment/9.3. Common Gear_.md` -- PDF 58 / p.56. A space before the full stop.
- [ ] "might be able perform their own repairs" -- `9. Equipment/9.12. Repairs & Crafting_.md` -- PDF 63 / p.61. Likely "able to perform".

## 12. Combat

- [ ] "until all allies have lead a first leg" -- `12. Combat/12.5. Chases_.md` -- PDF 74 / p.72. Likely "led".
- [ ] "makes a Perc (Det) check to notice to loss" -- `12. Combat/12.5.1. Chase Events.md` (row 5 i) -- PDF 75 / p.73. Likely "notice the loss".
- [ ] "split themselves.This may require" -- `12. Combat/12.5.1. Chase Events.md` (row 15) -- PDF 76 / p.74. No space after the full stop.
- [ ] "during other character's turns" -- `12. Combat/12.6. Action_.md` -- PDF 77 / p.75. Likely "characters'".
- [ ] "66% miss chance*" -- `12. Combat/12.7. Melee & Ranged Attacks_.md` (Melee/Ranged Modifiers) -- PDF 79 / p.77. The asterisk has no footnote on the page (possibly it points to Blind on p.82).
- [ ] "Cosmetic Scarring become Serious Scarring instead" -- `12. Combat/12.11. Conditions_.md` (Burning) -- PDF 84 / p.82. Likely "becomes". The Injuries & Setbacks rows are also titled "Scarring" (1-3) and "Disfigured" (13), not "Cosmetic Scarring" / "Serious Scarring".

## 13. Injury & Death

- [ ] The limb sub-rolls are punctuated inconsistently. In "Roll 1d6: 1-3 hand, 4-5: below elbow", the "1-3" has no colon but "4-5:" does. Likely "1-3: hand". Same pattern in:
  - "1-3 hand, 4-5: below elbow" -- `13. Injury & Death/13.1.1. Injuries & Setbacks.md` (row 18) -- PDF 86 / p.84
  - `13. Injury & Death/13.2.1. Blade Trauma.md` (row 10), `13. Injury & Death/13.2.2. Blast Trauma.md` (row 10), `13. Injury & Death/13.2.3. Blunt Trauma.md` (row 10), `13. Injury & Death/13.2.4. Missile Trauma.md` (row 10) -- PDF 86-89
  - "1d6: 1-3: foot" -- `13. Injury & Death/13.2.2. Blast Trauma.md` (row 11) -- PDF 87 / p.85. "Roll" is missing.
- [ ] "3d6 days of rest mends the injury" -- `13. Injury & Death/13.2.3. Blunt Trauma.md` (row 6) -- PDF 88 / p.86. No final full stop.
- [ ] "pre occupation" -- `13. Injury & Death/13.2.5. Toxin Trauma.md` (row 3) -- PDF 89 / p.87. Printed as two words at a line break, consistent with "non functional" etc. Likely "preoccupation" (low priority).

## 14. Healing & Recovery

- [ ] "predominately" -- `14. Healing & Recovery/14.3. Long Rest_.md` -- PDF 91 / p.89. Likely "predominantly".

## 15. Sorcery

- [ ] "A successful Int (Arcane Lore) check." -- `15. Sorcery/15.1. Spell Casting_.md` -- PDF 93 / p.91. The required-skill asterisk is missing. Elsewhere it is "Int (Arcane Lore*)", e.g. in `15. Sorcery/15.3. Sensing Magic_.md`.
- [ ] Title bar "DARK AND DANGEROUS MAGIC" vs section heading "DARK & DANGEROUS MAGIC" -- `15. Sorcery/15.5.1. Dark and Dangerous Magic.md` vs `15. Sorcery/15.5. Dark & Dangerous Magic_.md` -- PDF 94 / p.92. The vault follows each spelling. Unify the titles if you prefer.
- [ ] "They recede in 1d6 weeks" -- `15. Sorcery/15.5.1. Dark and Dangerous Magic.md` (row 8) -- PDF 94 / p.92. No final full stop.
- [ ] "your breath condensates" -- `15. Sorcery/15.5.1. Dark and Dangerous Magic.md` (row 13-14) -- PDF 94 / p.92. Likely "condenses".
- [ ] "Whisper of the Watchers" -- `15. Sorcery/15.5.1. Dark and Dangerous Magic.md` (row 29) -- PDF 95 / p.93. The spell is "Whispers of the Watchers". Possibly a deliberate variant.
- [ ] "Rift:" -- `15. Sorcery/15.5.1. Dark and Dangerous Magic.md` (row 61-62) -- PDF 96 / p.94. It has a colon where no other Rift row does.
- [ ] "(ii) Breathless (iii) Called From Below," -- `15. Sorcery/15.5.1. Dark and Dangerous Magic.md` (row 99) -- PDF 97 / p.95. A comma is missing after "Breathless", and row 27 is titled "Called from Below" (lower-case "from").
- [ ] "You catch a glimpse your patron's true form" -- `15. Sorcery/15.6.1. Divine Rebuke.md` (row 9-10) -- PDF 99 / p.97. Likely "a glimpse of".
- [ ] "the Consecrated Ground Rite of Atonement" -- `15. Sorcery/15.6.1. Divine Rebuke.md` (row 41-42) -- PDF 99 / p.97. The Rites of Atonement table (`15. Sorcery/15.7.1. Rites of Atonement.md`) has no rite by that name.
- [ ] "(even chance. If magical the item is damaged instead, not usable until repaired)" -- `15. Sorcery/15.6.1. Divine Rebuke.md` (row 78-80) -- PDF 100 / p.98. The full stop inside the parenthesis reads oddly. Likely "(even chance; if magical, ...)".
- [ ] "As Unchain the World Eater (p.231)" -- `15. Sorcery/15.6.1. Divine Rebuke.md` (row 100) -- PDF 100 / p.98. Printed p.231 is Valuables. The grimoire spell is on p.243 (PDF 245). The link now names the spell, so the vault no longer shows the page.
- [ ] "23-34 Crush of the Warp" -- `15. Sorcery/15.8.1. Spell List.md` -- PDF 102 / p.100. It overlaps 25-34. Likely "23-24".
- [ ] "Consult to Bones (likely)" -- `15. Sorcery/15.9. Spells/Beseech the Ancient Ones.md` -- PDF 105 / p.103. Likely "Consult the Bones".
- [ ] "the following . rules apply:" -- `15. Sorcery/15.9. Spells/Conjure Entity.md` -- PDF 106 / p.104. There is a stray full stop at the start of the line (visible on the page image).

## 16. Downtime

- [ ] "A minimum of spend of 20 sp" -- `16. Downtime/16.4. Carousing_.md` -- PDF 119 / p.117. Likely "A minimum spend of".
- [ ] "(i) Cutpurse Cinder Gribshanks (ii) Alchemist Lilian," -- `16. Downtime/16.4.1. Carousing.md` (row 27-28) -- PDF 120 / p.118. A comma is missing before "(ii)", and the "(ii)" is set inside the italic run.
- [ ] "burlsome brutes" -- `16. Downtime/16.4.1. Carousing.md` (row 47-48) -- PDF 121 / p.119. Not a standard word. Likely "burly" or "brawny".
- [ ] "Temple awaken on top of a temple roof" -- `16. Downtime/16.4.1. Carousing.md` (row 53-54) -- PDF 121 / p.119. Likely "You awaken".
- [ ] "You end up with of 1d3+1 adventure hooks" -- `16. Downtime/16.4.1. Carousing.md` (row 85-86) -- PDF 122 / p.120. Delete "of".
- [ ] "Desecrater" -- `16. Downtime/16.4.1. Carousing.md` (row 91-92) -- PDF 122 / p.120. Likely "Desecrator".
- [ ] "Poorly timed boasts of your many plunders reaches the ears" -- `16. Downtime/16.4.1. Carousing.md` (row 97-98) -- PDF 123 / p.121. Likely "reach".
- [ ] "(Blunt Trauma (1d6+6, but no permanent injuries)." -- `16. Downtime/16.5. Gambling_.md` -- PDF 123 / p.121. The parentheses are unbalanced.
- [ ] "44 Stubborn" and "44 Grumpy" -- `16. Downtime/16.6.1. Pet Qualities.md` -- PDF 124 / p.122. 44 is printed twice and 45 is missing. Likely "45 Grumpy".
- [ ] "Attempts to dissuade it provokes" -- `16. Downtime/16.6.2. Monstrous Instincts.md` (row 4) -- PDF 124 / p.122. Likely "provoke".
- [ ] Special Ingredient table -- `16. Downtime/16.7. Potion Brewing_.md` -- PDF 125 / p.123:
  - "Mend Flesh" sits out of alphabetical order (between Fire Aegis and Giant Strength), as do "One with the Deep" / "Transmogrification" / "Towering Growth" at the end.
  - "Dragon's Breath" (table) vs "Dragon Breath potion" (prose).
- [ ] "Two month's counselling" -- `16. Downtime/16.8. Recovery_.md` -- PDF 126 / p.124. Likely "Two months'".
- [ ] "GM's might permit" -- `16. Downtime/16.8. Recovery_.md` -- PDF 126 / p.124. Likely "GMs".
- [ ] "Rich or Filthy Rich Lifestyles include this cost, p.57)." -- `16. Downtime/16.8. Recovery_.md` (Persistent Injuries) -- PDF 126 / p.124. The closing parenthesis has no opening one. The vault reads "...include this cost)." because the page ref became a link.
- [ ] "the time and silver is lost" -- `16. Downtime/16.9. Research_.md` -- PDF 127 / p.125. Likely "are lost" (minor).
- [ ] "rumour table" -- `16. Downtime/16.10. Rumours_.md` -- PDF 128 / p.126. The prose refers to a rumour table, but none is printed in the book.
- [ ] "classic good or or resilient creatures" -- `16. Downtime/16.11. Scroll Inscribing_.md` (Scroll Materials, Protection) -- PDF 128 / p.126. "or" is doubled.

## 17. GM Tools

- [ ] "(patients as Str zero die)" -- `17. GM Tools/17.2.1. Diseases.md` (Slough Pox) -- PDF 133 / p.131. Likely "at Str zero".
- [ ] "chaffing feet" -- `17. GM Tools/17.2.1. Diseases.md` (Greyscale Blight) -- PDF 133 / p.131. Likely "chafing".
- [ ] "their vocal chords" -- `17. GM Tools/17.2.2. Parasites.md` -- PDF 133 / p.131. Likely "cords".
- [ ] "Throat leeches" -- `17. GM Tools/17.2.2. Parasites.md` -- PDF 133 / p.131. Lower-case "l", unlike every other entry name.
- [ ] "there's a few things the GM and party should consider" -- `17. GM Tools/17.3. Dungeon Crawling_.md` -- PDF 134 / p.132. Likely "there are" (minor).
- [ ] "ill fated prophesy" -- `17. GM Tools/17.4.4. Travel Events.md` (row 4) -- PDF 139 / p.137. Likely "prophecy".
- [ ] "one of the Lair's outer sentries have detected" -- `17. GM Tools/17.4.4. Travel Events.md` (row 16) -- PDF 140 / p.138. Likely "has".
- [ ] "torches, lantern, etc" -- `17. GM Tools/17.4. Hexploration_.md` -- PDF 141 / p.139. Likely "lanterns".
- [ ] "which ever occurs first" -- `17. GM Tools/17.4.5. Back to Base.md` (row 6) -- PDF 141 / p.139. Likely "whichever".
- [ ] "signalling an intention to parlay" -- `17. GM Tools/17.5.1. Aerial.md` -- PDF 142 / p.140. Likely "parley".
- [ ] "A once a millennia full solar or lunar eclipse" -- `17. GM Tools/17.5.1. Aerial.md` -- PDF 142 / p.140. Likely "millennium".
- [ ] "(player draws from the Deck of Signs: If a sun, ... or if a moon they lose 1 Luck instead." -- `17. GM Tools/17.5.2. City, Town, Village.md` (row 51-52) -- PDF 144 / p.142. The parenthesis is never closed.
- [ ] "etc for discrete clientele" -- `17. GM Tools/17.5.2. City, Town, Village.md` (row 67-68) -- PDF 144 / p.142. Likely "discreet".
- [ ] "staggers in a cluttered ally and collapses" -- `17. GM Tools/17.5.2. City, Town, Village.md` (row 73-74) -- PDF 145 / p.143. Likely "alley".
- [ ] "They are guardians of a scared site" -- `17. GM Tools/17.5.3. Deserts.md` (row 19) -- PDF 146 / p.144. Likely "sacred".
- [ ] "A Blue Hag (as Hag, but amphibious and Spells (3)" -- `17. GM Tools/17.5.7. Oceans, Lakes, Rivers.md` (row 11) -- PDF 151 / p.149. The "(as" is never closed.
- [ ] "(vi) tools, (vii) wheat, (iv) iron." -- `17. GM Tools/17.5.9. Roads & Trails.md` (row 5) -- PDF 152 / p.150. Likely "(viii) iron".
- [ ] "The undertaker might be Doppelganger" -- `17. GM Tools/17.5.9. Roads & Trails.md` (row 14) -- PDF 153 / p.151. Likely "a Doppelganger" (minor).
- [ ] "with a carriage or textiles wagons, secreting transporting, 1d8:" -- `17. GM Tools/17.5.9. Roads & Trails.md` (row 15) -- PDF 153 / p.151. The wording is garbled. Likely "secretly transporting".
- [ ] "(as Giant Serpent but Swim Close, and electric shock (Luck (Con) save or Stunned instead of poison) emerge" -- `17. GM Tools/17.5.11. Swamps.md` (row 14) -- PDF 156 / p.154. The outer parenthesis is never closed.

## 18. Hirelings

- [ ] "(vi) thug (vii) ex-pirate (viii) green recruit." -- `18. Hirelings/18.2. Backgrounds_.md` -- PDF 159 / p.157. Commas are missing after "thug" and "ex-pirate".
- [ ] "Loose Canon" -- `18. Hirelings/18.3.1. Personality.md` (row 1-3) -- PDF 159 / p.157. Likely "Loose Cannon".
- [ ] "Storm's brewin'" -- `18. Hirelings/18.5.2. Catchphrase.md` (row 83-84) -- PDF 161 / p.159. No closing full stop, unlike every other row.

## 20. Mass Battle

- [ ] "(vi) Nets." -- `20. Mass Battle/20.1.1. Field Events.md` (row 3) -- PDF 164 / p.162. Capitalised in the middle of the list.
- [ ] "a nameless solider automatically intervenes" -- `20. Mass Battle/20.2.1. Sudden Twist.md` (row 13) -- PDF 167 / p.165. Likely "soldier".

## 21. Monsters

- [ ] `**Spiked Carapac**e` -- `21. Monsters/21.4. Bestiary/Mutations.md` (row 3) -- PDF 204 / p.202. The bold stops one letter short in both the print and the font data. Likely `**Spiked Carapace**`.
- [ ] Reaction (Reac) ranges that overlap or leave a gap:
  - "5-6 Haughtily annoyed 6-8 Languidly indifferent" (6 twice) -- `21. Monsters/21.4. Bestiary/Cat.md` -- PDF 173 / p.171
  - "9-10 Wary 10-12 Interested" (10 twice) -- `21. Monsters/21.4. Bestiary/Beetle, Fire.md` -- PDF 177 / p.175
  - "8-9 Covetous 11-12 Inquiring" (10 missing) -- `21. Monsters/21.4. Bestiary/Cyclops.md` -- PDF 178 / p.176
  - "7-9 Grumpy 9-12 Cautious" (9 twice) -- `21. Monsters/21.4. Bestiary/Elemental, Earth.md` -- PDF 183 / p.181
  - "9-10 Withdrawn 10-12 Interested" (10 twice) -- `21. Monsters/21.4. Bestiary/Goblin.md` -- PDF 186 / p.184
  - "9-10 Civil 10-12 Captivated" (10 twice) -- `21. Monsters/21.4. Bestiary/Lich.md` -- PDF 191 / p.189
  - "2-3 Hostile 5-7 Famished" (4 missing) -- `21. Monsters/21.4. Bestiary/Rust Monster.md` -- PDF 198 / p.196
- [ ] "Impart Sorcery: targets rolls" -- likely "target rolls":
  - "targets rolls" -- `21. Monsters/21.4. Bestiary/Lich.md` -- PDF 191 / p.189
  - "targets rolls" -- `21. Monsters/21.4. Bestiary/Wight.md` -- PDF 206 / p.204
  - "targets rolls" -- `21. Monsters/21.4. Bestiary/Wraith.md` -- PDF 207 / p.205
- [ ] Unbalanced parentheses in stat blocks:
  - "Frenzies when they or target is Wounded: Bite (2) per action)." -- `21. Monsters/21.4. Bestiary/Shark.md` -- PDF 174 / p.172
  - "Limb torn off (Luck (Dex) save resists S19" -- `21. Monsters/21.4. Bestiary/Owlbear.md` -- PDF 196 / p.194
  - "Poison: 1d4 Str loss (Luck) Con save for half" -- `21. Monsters/21.4. Bestiary/Roper.md` -- PDF 198 / p.196. The parenthesis is misplaced. Elsewhere it reads "Luck (Con) save".
  - "might tip off an observer." (the opening "(indistinguishable from a normal vine, but" is never closed) -- `21. Monsters/21.4. Bestiary/Vine Puppet.md` -- PDF 206 / p.204
- [ ] Missing full stop before **Reac** or at the end of a stat line:
  - "save or suffer Lycanthropy Reac" -- `21. Monsters/21.4. Bestiary/Lycanthrope, Werebear.md` and `21. Monsters/21.4. Bestiary/Lycanthrope, Werewolf.md` -- PDF 192 / p.190 (Wererat has the full stop)
  - "Move Far Reac" -- `21. Monsters/21.4. Bestiary/Ogre Mage.md` -- PDF 195 / p.193
  - "Climb Close Reac" -- `21. Monsters/21.4. Bestiary/Mimic.md` (PDF 193) and `21. Monsters/21.4. Bestiary/Ooze, Grey.md` (PDF 196)
  - "Psychic Force Reac" -- `21. Monsters/21.4. Bestiary/Tentacle Spawn.md` -- PDF 203 / p.201
  - "9-12 Oblivious" -- `21. Monsters/21.4. Bestiary/Octopus, Giant.md` -- PDF 195 / p.193 (end of the stat block)
- [ ] "detailed on p.170 Three example creatures appear below." -- `21. Monsters/21.4. Bestiary/Lycanthropes.md` -- PDF 192 / p.190. There is no full stop after "p.170".
- [ ] "weigh more than a 1,500 pounds" -- `21. Monsters/21.4. Bestiary/Bear.md` -- PDF 173 / p.171. The "a" is stray.
- [ ] "knocked prone" -- `21. Monsters/21.4. Bestiary/Centaur.md` -- PDF 177 / p.175. Lower-case and not italic, where the condition is elsewhere *Prone* (consistency only).
- [ ] "they may subtlety skim the surface thoughts" -- `21. Monsters/21.4. Bestiary/Doppelganger.md` -- PDF 181 / p.179. Likely "subtly".
- [ ] "Fly Normal" -- `21. Monsters/21.4. Bestiary/Ghost.md` -- PDF 185 / p.183. "Climb Normal" -- `21. Monsters/21.4. Bestiary/Ghoul.md` -- PDF 185 / p.183. Every other stat block uses "Norm".
- [ ] "shiny things which they horde" -- `21. Monsters/21.4. Bestiary/Merscine.md` -- PDF 193 / p.191. Likely "hoard".
- [ ] Climb is given twice in the stat block, as "Climb Norm." and later "Climb Close" -- `21. Monsters/21.4. Bestiary/Mimic.md` -- PDF 193 / p.191.
- [ ] "basic emotions such love, fear" -- `21. Monsters/21.4. Bestiary/Ooze, Grey.md` -- PDF 196 / p.194. Likely "such as".
- [ ] "come in a various forms" -- `21. Monsters/21.4. Bestiary/Ooze, Sentient.md` -- PDF 196 / p.194. Likely "come in various forms".
- [ ] "lurking in forests nearby civilization" -- `21. Monsters/21.4. Bestiary/Rat, Giant.md` -- PDF 197 / p.195. Likely "near civilization" (minor).
- [ ] "For Giant Serpents see p.192" -- `21. Monsters/21.4. Bestiary/Snake.md` -- PDF 174 / p.172. Printed p.192 holds Monkey/Minotaur/Mummy/N'Tarc. Giant Serpent is on p.196-197 (PDF 198-199).
- [ ] "lust for a small glittering things" -- `21. Monsters/21.4. Bestiary/Sprite.md` -- PDF 202 / p.200. The "a" is stray.
- [ ] "an ambush laying prone" -- `21. Monsters/21.4. Bestiary/Vine Puppet.md` -- PDF 206 / p.204. Likely "lying".
- [ ] "A Xornling left to its own devices will eat 1d10 coins..." -- `21. Monsters/21.4. Bestiary/Xornling.md` -- PDF 208 / p.206. The sentence is printed twice (in the description and again in the stat block). Both copies are kept.

## 22. Naval Combat

- [ ] "Navel Combat is divided" -- `22. Naval Combat/22.1. Naval Combat_.md` -- PDF 210 / p.208. Likely "Naval".
- [ ] "between ship statistics may may result in modifiers" -- `22. Naval Combat/22.2. Ships_.md` -- PDF 210 / p.208. "may" is doubled.
- [ ] "To reflect his, one PC rolls" -- `22. Naval Combat/22.5. Boarding_.md` -- PDF 212 / p.210. Likely "this".
- [ ] "drops a weighed net" -- `22. Naval Combat/22.5.1. Boarding.md` (row 17) -- PDF 213 / p.211. Likely "weighted".
- [ ] "(Consult the Bones, or GM's call)" -- `22. Naval Combat/22.5.1. Boarding.md` (row 20) -- PDF 213 / p.211. No closing full stop.

## 23. Oracle Tools

- [ ] "The cards also includes a small compass symbol" -- `23. Oracle Tools/23.3. Read the Signs_.md` -- PDF 215 / p.213. Likely "include".

## 25. Solo Rules

- [ ] "light sleeper, etc).This is a bonus Travel Role" -- `25. Solo Rules/25.2. Lone Wolf_.md` -- PDF 218 / p.216. No space after the full stop.
- [ ] "Alternatively, to create a map as you go see p.220" -- `25. Solo Rules/25.4. Dungeon Generator_.md` -- PDF 220 / p.218. No final full stop.
- [ ] "place secret door or hatch" -- `25. Solo Rules/25.4. Dungeon Generator_.md` -- PDF 222 / p.220. Likely "place a secret door".
- [ ] "any modifiers are GM's call)" -- `25. Solo Rules/25.4.10. Room Contents.md` (row 11) -- PDF 222 / p.220. No closing full stop.
- [ ] "Concealed 1-3 Info 4-9 Valuables B 10-13 Minor Magical Item, 14-17 Door 18-20 Special." -- `25. Solo Rules/25.4.11. Theme Items.md` (Secret) -- PDF 223 / p.221. It looks as if "Concealed Door" (14-17) was split by the layout. Likely "1-3 Info ... 14-17 Concealed Door ...".

## 26. Traps

- [ ] "Minor Poison p.222" (all three rows) -- `26. Traps/26.4.12. Gas.md` -- PDF 227 / p.225. Printed p.222 is the Traps opener. The Poison table is on p.226 (`26. Traps/26.4.18. Poison.md`). The page refs were left unlinked for this reason.
- [ ] Rows with no final full stop:
  - "before the room seals" (Major) -- `26. Traps/26.4.10. Drowning.md` -- PDF 227 / p.225
  - "Moderate (40%) or Major (60%) Poison p.222" (Major) -- `26. Traps/26.4.12. Gas.md` -- PDF 227 / p.225
  - "(1d12)" (Minor) -- `26. Traps/26.4.16. Needle.md` -- PDF 228 / p.226
  - "(50/50)" (Major) -- `26. Traps/26.4.17. Pit.md` -- PDF 228 / p.226

## 27. Treasure

- [ ] Missing commas in the gem and item lists:
  - "(iii) Amber (iv) Turquoise" -- `27. Treasure/27.1.1. Carry Loot A.md` (row 86-95) -- PDF 231 / p.229
  - "(v) Emerald (vi) Peridot", "(ix) Ruby (x) Diamond" -- `27. Treasure/27.1.2. Carry Loot B.md` (row 86-95) -- PDF 232 / p.230
  - "(iii) Amber (iv) Turquoise" -- `27. Treasure/27.2.1. Valuables A.md` (row 61-70) -- PDF 233 / p.231
  - "(i-vii) Weapon (viii-ix) Armour" -- `27. Treasure/27.2.1. Valuables A.md` (row 71-77) -- PDF 233 / p.231
- [ ] "a silver ivy motif ring (70 sp)" -- `27. Treasure/27.2.1. Valuables A.md` (row 10-12) -- PDF 232 / p.230. No final full stop.
- [ ] "a bronze circlet decorated with opals (570 gp)" -- `27. Treasure/27.2.2. Valuables B.md` (row 18-21) -- PDF 233 / p.231. Every other value is in sp. Likely "570 sp".
- [ ] "old title deeds to Eventide Isle, located in one of the larger inlets of Lake Argos." -- `27. Treasure/27.2.2. Valuables B.md` -- PDF 234 / p.232. No value is printed, unlike every other item.
- [ ] "tiny black writing can see be seen along the shaft" -- `27. Treasure/27.3.1. Trinkets & Curios.md` (row 1) -- PDF 234 / p.232. Delete "see".
- [ ] "the Harlot is in more debt than its worth" -- `27. Treasure/27.3.1. Trinkets & Curios.md` (row 6) -- PDF 234 / p.232. Likely "it's".
- [ ] "depicts a pair mesmerizing snake eyes" -- `27. Treasure/27.3.1. Trinkets & Curios.md` (row 11) -- PDF 235 / p.233. Likely "a pair of".
- [ ] "a wild dog with a one eye" -- `27. Treasure/27.3.1. Trinkets & Curios.md` (row 13) -- PDF 235 / p.233. Likely "with one eye".
- [ ] "(Close range, silent, 1 damage + Poison. 420 sp)" -- `27. Treasure/27.3.1. Trinkets & Curios.md` (row 26) -- PDF 236 / p.234. A full stop where a comma is expected.
- [ ] "glass jar" ... "the bottle explodes" -- `27. Treasure/27.3.1. Trinkets & Curios.md` (row 34) -- PDF 236 / p.234. The item changes from a jar to a bottle.
- [ ] "If the owner fails an Death save" -- `27. Treasure/27.3.1. Trinkets & Curios.md` (row 47) -- PDF 237 / p.235. Likely "a Death save".
- [ ] "made of basalt stone. (26 sp)." -- `27. Treasure/27.3.1. Trinkets & Curios.md` (row 95) -- PDF 239 / p.237. There is a full stop before the price.
- [ ] Lair Treasure sidebar: "the ancient wilds and lost ruins adventurers tend to explore expose them to" reads oddly but may be intended. "Lair treasure" is lower-case here, where elsewhere it is "Lair Treasure" -- `27. Treasure/27.4. Lair Treasure_.md` -- PDF 240 / p.238 (low priority).
- [ ] "they have nevertheless been wrapped into in the Spellbooks category" -- `27. Treasure/27.5. Minor Magical Items_.md` -- PDF 241 / p.239. Delete "in".
- [ ] "34-56 Mend Flesh" -- `27. Treasure/27.5.2. Potions.md` -- PDF 242 / p.240. The next row is 57-59. Likely "34-36".
- [ ] "81-83 Sharpened Senses" / "83-85 Sight Beyond Sight" -- `27. Treasure/27.5.2. Potions.md` -- PDF 242 / p.240. 83 is in both rows. Likely "81-82" or "84-85".
- [ ] "As the Old Magic Grimoire spell (p.230)" -- `27. Treasure/27.5.2. Potions.md` (row 89-91, Starmaiden's Miracle) -- PDF 242 / p.240. The spell is on p.242 (PDF 244). Printed p.230 is Carry Loot B / Valuables A. Left unlinked.
- [ ] "(p.226)" -- `27. Treasure/27.5.2. Potions.md` (row 72-74) -- PDF 242 / p.240. No final full stop. The page ref is now a link to the Poison table.
- [ ] "with this dread incanter" -- `27. Treasure/27.6. Old Magic Grimoires/Word of Ending.md` -- PDF 245 / p.243. Likely "incantation".
- [ ] "and adopts pirate phrases" ... "Aye, cap'ain" -- `27. Treasure/27.7.1. Minor Charms.md` (row 67-68) -- PDF 248 / p.246. The subject is "you", so likely "adopt". "cap'ain" is likely "cap'n".
- [ ] "and drinks from the cup" -- `27. Treasure/27.7.1. Minor Charms.md` (row 69-70) -- PDF 248 / p.246. With "you", likely "drink".
- [ ] "Yulnvorg the Bonebreaker p.251" -- `27. Treasure/27.8.1. Major Magical Items.md` (row 6) -- PDF 251 / p.249. The circumflex is missing. The entry is "Yûlnvorg" (`27. Treasure/27.8. Major Magical Items/Yûlnvorg the Bonebreaker.md`).
- [ ] "but the forge work ancient in nature" -- `27. Treasure/27.8. Major Magical Items/Storm Spear.md` -- PDF 251 / p.249. Likely "is ancient".
- [ ] "You may treat the casting as a Great Success, is desired." -- `27. Treasure/27.8. Major Magical Items/Cowl of the North.md` (3rd) -- PDF 252 / p.250. Likely "if desired".
- [ ] "At any later time, you user may spend an action" -- `27. Treasure/27.8. Major Magical Items/Talisman of the Black Sun.md` (1st) -- PDF 253 / p.251. Likely "the user" or "you".
- [ ] "under some other thick cover (forest canopy, etc)." -- `27. Treasure/27.8. Major Magical Items/Staff of Mensicor.md` (Special) -- PDF 253 / p.251. The outer "(-2 penalty ..." parenthesis is never closed.
- [ ] "sound the horn for over the course of 1 hour" -- `27. Treasure/27.8. Major Magical Items/Horn of Karagoss.md` (3rd) -- PDF 254 / p.252. Delete "for" or "over the course of".
- [ ] "Careful examination suggests the your breathing is irregular." -- `27. Treasure/27.8. Major Magical Items/Torc of Sebutett.md` (1st) -- PDF 255 / p.253. Delete "the".
- [ ] "This fine cooper brooch" -- `27. Treasure/27.8. Major Magical Items/Plague Demon's Clasp.md` -- PDF 256 / p.254. Likely "copper".
- [ ] "Whist in two dimensional shadow form" -- `27. Treasure/27.8. Major Magical Items/Dusker's Vest.md` (3rd) -- PDF 257 / p.255. Likely "Whilst".
- [ ] "Check for a DMM effect" -- `27. Treasure/27.10.6. Obvious Powers.md` (row 95-96) -- PDF 260 / p.258. Likely "DDM".
- [ ] "Telepathic you may send" (row 7-9, PDF 260) and "Jack of All Trades you count" (row 34-36, PDF 261) -- `27. Treasure/27.10.7. Discreet Powers.md`. Lower-case after the bold name, unlike every other row. Likely "You".
- [ ] Generator title: the title bar is MAJOR ITEM GENERATOR (vault note `27. Treasure/27.10. Major Item Generator_.md`, PDF 258), but the contents page and `28. Variant Rules/28.2. Conversion Tips_.md` (PDF 263) say "Magic Item Generator". Heavy Abilities #18 (`21. Monsters/21.3.1. Heavy Abilities.md`) says "Item Generator". The 28.2 reference is unlinked for this reason.

## 28. Variant Rules

- [ ] "New skill at 11th level," -- `28. Variant Rules/28.1. Variant Rules_.md` (Advancement beyond 9th level) -- PDF 262 / p.260. A comma where a full stop is expected.

## Open questions for the formatting pass

These are judgement calls made during transcription or linking. They are not errors, and each can be changed.

**Tables and headers**

- [ ] `16. Downtime/16.9.1. Standard Research.md`: the first header cell "Int check" is not printed (the frame has only the STANDARD RESEARCH title bar). It is inferred from the prose "an Int check is required". Keep it, or leave the cell empty?
- [ ] `27. Treasure/27.4.1. Lair Treasure.md` is a lookup by HD, not a roll. It was kept as a table note because every cell is a treasure roll. You could move it into `27. Treasure/27.4. Lair Treasure_.md` as a reference table.
- [ ] `17. GM Tools/17.4.1. Fortune Die Examples.md` is a numbered 1-8 list of examples ("Use the opposite for Misfortunes"). It was written as a roll table with an inferred d8. It could become a plain list in `17. GM Tools/17.4. Hexploration_.md`.
- [ ] `21. Monsters/21.2.1. Monsters by HD.md`: the HD band is the first column (header "HD", borrowed from the adjacent Custom Monsters table) and each band's numbered monster list is one cell. No die is printed (the lists run 1d11, 1d16, 1d24, ...).
- [ ] `24. Rival Adventurers/24.1. Rival Adventurers_.md`: the class table repeats its header on p.217, which was dropped. Each class takes three rows, with the class cell (name + attribute lines, `<br>`) filled only in the first row. Alternatives: repeat the class name on every row, or use one table per class.
- [ ] `17. GM Tools/17.4.4. Travel Events.md`: cells printed spanning OVERLAND/UNDERGROUND/VOYAGE are repeated in each column they span (Markdown has no colspan).
- [ ] `18. Hirelings/18.5.1. Hireling Gear.md`: the header is "d4/d12" (non-combatants roll 1d4 on rows 1-4, mercenaries 1d12), and the Non-Combatant / Mercenary lines in rows 1-4 are joined with `<br>`.
- [ ] `25. Solo Rules/25.4.11. Theme Items.md`: the header is `| | d20 |`. Column 1 holds the theme names and column 2 the inline d20 sub-ranges.
- [ ] `15. Sorcery/15.5.1. Dark and Dangerous Magic.md`: the two footnote markers are written `<sup>1</sup>` / `<sup>2</sup>` (16 instances, the only `<sup>` in the vault). The print sets them bold. If you want strict bold, write `**<sup>1</sup>**`.
- [ ] Roll numbers print bold in the book but are plain in every table note, following the approved sample (`13.2.1. Blade Trauma`).
- [ ] Possible extra roll tables that were left as reference tables or inline prose (promote if you want them rollable):
  - Melee Weapons (d20), Ranged Weapons (d6), Animals (d8) and Vehicles & Ships (d8) in `9. Equipment/`
  - Ships (d8) and Blackpowder Weapons (d4) in `22. Naval Combat/`
  - Session Advance (d10) in `16. Downtime/16.2. Advancement_.md`
  - the inline lists for Race (1d12), Rare Gear (1d20), random armour (1d6), Minor Exploits (1d6), mercenary backgrounds (1d8) and the Potions container (1d6)

**Placement and structure**

- [ ] `26. Traps/26.4. Simple Traps_.md`: the 20 trap-mode embeds (Acid ... Spear, Spikes) follow the numbered order, after `#### Cost`, so in the outline they sit under "Purchasing Traps". The R2 triage reads p.228 as printing Magic, Poison, Monster, Pit, Needle (with the Poison lead-in before Magic). A8 numbered them left column then right. Options: move all 20 embeds under `### Mode of Attack`, and/or re-check the p.228 order.
- [ ] `20. Mass Battle/20.2. Sudden Twists_.md` and `20. Mass Battle/20.3. Final Confrontation_.md`: each whole section is a parchment box in print. They are written as plain paragraphs, not as `> [!note]`, to avoid repeating the title. Wrap them in a callout if you prefer.
- [ ] Boxed headings written as callouts, so they don't appear in the outline: "Delay & Ready Action" (`12. Combat/12.1. Initiative & Turn Order_.md`), "Readied Gear" and "Travel Procedure" (`17. GM Tools/17.3. Dungeon Crawling_.md`, `17. GM Tools/17.4. Hexploration_.md`), "Carry Loot A" (`27. Treasure/27.1. Treasure_.md`).
- [ ] The Designer's Thoughts box on PDF 250 is at the end of `27. Treasure/27.9. Attunement & Using Powers_.md`, where it prints (the plan had it under 27.8).
- [ ] `27. Treasure/27.6. Old Magic Grimoires_.md` holds only the Designer's Thoughts box, beside the `27.6. Old Magic Grimoires/` folder. It could move into 27.5.
- [ ] `15. Sorcery/15.8. Spell List_.md` is a stub holding only the embed (no prose is printed).
- [ ] The Graxus Common Phrases / Icons lines (`5. Classes/5.5. Example Gods/Graxus (The Iron God).md`) print as two short lines each. They are joined into one paragraph and could use hard breaks.
- [ ] The Alchemy & Mechanica OPTIONAL entry "13. Poison" is kept in the `> [!tip] Optional` callout in `5. Classes/5.2. Artificer_.md`, not in the d12 table.

**Linking (2026-11-25)**

- [ ] *Reroll(s)*, *cold iron*, *silvered*, *adamantine* and *mithral* are left unlinked everywhere, like *Luck* (36 links removed to make the groups consistent). If you want them linked, the targets would be `8. Skills & Rerolls/8.2. Rerolls_.md` and `9. Equipment/9.9. Weapons_.md` (heading Special Metals).
- [ ] Spelling mismatches that blocked links (see Book-wide above): Hraarsk/Hraask, Ssurlock/Ssurloc, Wing Snake/Winged Snake, and Hell Hound/Hellhound (Monsters by HD links "Hell Hound" to `Demon, Hellhound`, but the spell/potion/scroll mentions are unlinked). "Magic Item Generator" in 28.2 is unlinked.
- [ ] Bad printed pages left as printed (no link): Gas "Poison p.222", Potions 89-91 "(p.230)", Snake "see p.192".
- [ ] Ambiguous references left unlinked:
  - "Illusions cannot be detected in this way (p.91)" (`5. Classes/5.7. Magic User_.md`; 15.3 or 15.4?)
  - *Carry Loot* (`7. Unique Features/7.2. Example Unique Features/Born to Loot.md`; A or B?)
  - Shield of Argaunt "requiring repair (p.61)" (9.11 or 9.12?)
  - *Broken Ribs* (Blunt Trauma #6 or Injuries & Setbacks #14?) in Ape, Bear, Golem, Stone, Owlbear, Rhino
  - bare *Old Magic Grimoires* (27.5.3 or 27.6?)
  - *Lightning* (`21. Monsters/21.4. Bestiary/Golem, Flesh.md`)
  - "the injury tables", "the Hireling tables", "Class Attack Bonus & Abilities tables", "rumour table", "Treasure chapter", "Magic chapter", and 10.2 "(see Contests below)" (probably 10.4 Opposed Checks)
- [ ] Names with no matching note, left plain:
  - *Undead* outside chapter 21 (there is no Undead note; inside chapter 21, L6 linked it to the heading `21.3. Special Traits_#Demons & Undead`)
  - *Dire Wolf(s)*, *Dire Rats*, *Dire Bats*, *Aberrations*, *Infernal Minotaur*, *Urgozer*, *Deck of Signs*, *Rift* (DDM row)
  - table rows used as names: *Fork the River*, Alchemy/Blessings/Adaptable/Monk/Rangercraft/Tricks entries in 24.1, *Lemon Rot*, *Muscle Tear*, *Nasty Scars*, *Severed Arm or Leg*
  - setting NPCs and places
  - "Spike trap" (Relocation; the note is Spear, Spikes)
- [ ] Inflected and inverted names were linked by meaning (e.g. Giant Eagles -> `Eagle, Giant`, Sabretooth Tiger -> `Tiger`, Moor Trolls -> `Troll`, Desert Bulette -> `Bulette`, Dire Wolf -> two links, `Dire Animal` + `Wolf (or Dog)`). Review if you'd rather link exact names only.
- [ ] The vault-wide rule leaves the italic resource words (*Luck*, *Reroll*) plain. Two links remain by design: "see *Luck*" (`10. Doing Things/10.1. Doing Things_.md`, an explicit "see X") and "adamantine shield" -> `9. Equipment/9.11. Shields_.md` (consumes "(p.61)" in `9. Equipment/9.15.2. Masterforged Armour.md`).

## Checker flags judged to be false alarms

- "Medium,Wood" (Buildings table, `16. Downtime/16.1. Downtime_.md`, PDF 115). R1 read it as a missing space. The page image shows "Medium, Wood" with a tight space, so the note is correct.
- Text-layer glitches, written as the image shows: "roof 's" (PDF 8), "mayonly" (PDF 25), "THIEVES ' GRACE" (PDF 52), "BALLARD ' S BLADE" (PDF 252), "WOLF (0r DOg)" (PDF 174), "Thief ! Thief !" (PDF 144), `**N**'**TARC**` (PDF 194), "a\n-\n1 XP" (PDF 117), a stray "." (PDF 88) and a stray "WEAPON" token (PDF 216) that are not on the page.
- Skill asterisks with no footnote, e.g. "Dex (Acrobatics*)" (PDF 72, 84), "Str (Athletics*)" (Lockdown, PDF 227) and "Int (Wilderness Lore*)" (Trinkets 36, PDF 236). These follow the book's convention that an asterisk marks a *required* skill (`8. Skills & Rerolls/8.1. Skills_.md`). "Arrows typically use Ammo rolls*" (PDF 58) matches "Arrows (20*)" in the Common Gear table.
- "#61" in "Precious Stone #61 Valuables A", "Gemstone #61 Valuables B" (`27. Treasure/27.10.4. Miscellaneous.md`) and "Gemstones Valuables B #61" (`25. Solo Rules/25.4.4. Reward.md`). These are valid references to row 61-70 (the gem rows) of the Valuables tables, not page numbers.
- Fidelity "emphasis" / "table-emphasis" flags (e.g. Carousing "one week", Potions "Starmaiden's Miracle", Dungeon Generator "site", Carry Loot "carry loot"). The checker aligned text against neighbouring tables or embed lines. Rechecked against the font data: no mismatch. The only real one, Artificer "13. Poison", was patched (R1).
- Fidelity "words" / "reordered" / "moved" / "not-in-text-layer" flags. These come from embedded roll-table rows (the rows live in the table notes), titles carried by filenames, running heads and page numbers, two-column reading order, bracketed icon words, and page-range limits in the checker (4.1 Races_, 9.10 Armour_).
- Fidelity "no-source-match" on 9 table notes (e.g. Pet Qualities, Weather Shift, Personality, Dungeon Site, Main Opposition, Spell Like Blessings, Jewellery, Clothing, Spell List_). The table check located each one on its page by hand (T12).
- Table check: "cell-spans-rows", "text-between-rows", "cell-cut-short", "header-unlocated", "row-cells-apart" and "cell-misplaced". These are layout noise from vertically centred die numbers, side-by-side halves and interleaved columns. Every row was confirmed on the page images.
- Coverage: 44 pages with "unexplained words". These are stat-block tokens split differently ("c12" = `**C**12`) on the Ranger beast companions (PDF 41) and bestiary pages (PDF 173-209), "monster1"/"spell2" (the DDM footnote markers written as `<sup>`), "vengeful" (an entry heading carried by the filename) and "mayonly" (fixed to "may only").
- Structure: "NO-H1" on every note (by design, since the filename carries the title) and "SHORT" on `15. Sorcery/15.8. Spell List_.md` (an embed-only stub).
- "super natural" (DDM 51-52), "non functional", "self heal": the book's own spacing style at line breaks, not errors.
