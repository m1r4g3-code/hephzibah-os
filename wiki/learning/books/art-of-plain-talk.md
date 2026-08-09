---
sensitivity: public

entity_type: book
name: The Art of Plain Talk
author: Rudolf Flesch
aliases: [art-of-plain-talk, flesch-plain-talk]
last_updated: '2026-08-09'
relationships:
- target: '[[identity]]'
  type: on_reading_list
  strength: 5
  first_seen: '2026-08-09'
  last_reinforced: '2026-08-09'
- target: '[[cold-outreach]]'
  type: informs
  strength: 6
  first_seen: '2026-08-09'
  last_reinforced: '2026-08-09'
- target: '[[specificity-as-credibility]]'
  type: related_to
  strength: 5
  first_seen: '2026-08-09'
  last_reinforced: '2026-08-09'
type: book-note
---

Rudolf Flesch, 1946. The book that laid the groundwork for the Flesch Reading Ease score — this is the earlier, rawer version of that research, written as a practical how-to rather than a formula reference. 223 pages, 22 chapters plus an appendix showing how to run the difficulty formula by hand.

## Core Thesis

Clear writing and speaking is not a talent or a personality trait — it's a mechanical property of language that can be measured and engineered. Most advice on "writing simply" (use short words, be direct, etc.) is vague and unfalsifiable. Flesch's claim: you can score any piece of writing for difficulty using three measurable variables — sentence length, affix density, and the ratio of "personal" (human) words to abstract ones — and then deliberately rewrite toward the easy end of that scale. Simplicity isn't dumbing down; it's removing the friction between what's in your head and what lands in the reader's.

## The Concrete Techniques

**1. The Yardstick Formula (Ch. VII, Appendix)**
Difficulty score = (average sentence length × .1338) + (affixes per 100 words × .0645) − (personal references per 100 words × .0659) − .75.
Score bands: under 1 = Very Easy, 1–2 Easy, 2–3 Fairly Easy, 3–4 Standard, 4–5 Fairly Difficult, 5–6 Difficult, 6+ Very Difficult. Flesch runs this on an actual Lend-Lease treaty clause (81-word average sentence, 57 affixes/100 words, zero personal references) and scores it 13.77 — "completely unreadable diplomatic double talk" — then walks it down to plain English step by step: break sentences first, then strip affixes back to root words, then add people back in.

The appendix gives the exact counting rules: sample every third paragraph (don't cherry-pick "typical" ones), count to the ~100-word mark, count sentences by unit of thought (not punctuation — semicolons can end a "sentence" for this purpose), count affixes against a fixed list (excludes plural -s, possessive -s, verb -ed on modals like *could/would*), count personal references as three types only: names, personal pronouns, and a closed list of relationship words (man, woman, father, friend, etc. — not "teacher" or "doctor," which don't count even though they're people).

**2. Sentences come first, not words (Ch. IV)**
A sentence = one thought. Two thoughts need two sentences. The failure mode is "tangled" sentences where a clause is tied back to a word many words away (his example: "*Here is Edmund Burke, the eminent British Liberal, than whom no European statesman was more horrified...*" — the reader has to hold "whom" in memory across an intervening clause). Fix: break the sentence at the tangle point and restate the subject.

**3. Live words — use verbs (Ch. VIII)**
"Use verbs. Let me repeat that: use verbs." The only words with "life" in them are finite active verb forms — not participles, infinitives, or gerunds, which Flesch says are grammatically verbs but functionally nouns/adjectives. Passive voice and nominalized verbs ("the actualization of solidarity") drain sentences of motion. His test: read a passage and count the truly active, "kicking" verbs — most bad nonfiction runs almost entirely on passives and abstractions.

**4. Crowded words — kill the comments (Ch. IX)**
Distinguishes *defining* adjectives (part of the noun: "math teacher") from *commenting* adjectives (hostile to the noun they modify: "a ravishing math teacher" — you remember "ravishing," not "teacher"). Rule: don't rescue an overloaded sentence by stuffing a comment into it — split it into two simple sentences instead. "Two short sentences are easier to understand than one long one with extra stuff in it."

**5. Empty words — cut compound prepositions (Ch. X)**
A hit list of inflated phrases to replace with their one-word equivalents: *along the lines of* → like, *for the purpose of* → for, *in the event that* → if, *with regard to* → about, *prior to* → before, *inasmuch as* → since, *in order to* → to. Each "empty word" (preposition/conjunction/adverb) adds grammar the reader has to process; every one you cut saves real effort at the receiving end.

**6. Punctuation is a spoken-pause map, not a rulebook (Ch. XI)**
Maps punctuation directly onto speech: normal pause → white space/period; shorter pause → hyphen/semicolon; longer pause → dash/paragraph break. In plain talk specifically, hyphens and semicolons matter most — hyphens because fewer empty words means word order has to carry more of the meaning, and semicolons because plain talk favors several short sentences chained together over one long one.

**7. Advertising copy as the readability lab (Ch. XVIII)**
Flesch treats ad copywriters as the group who actually tested this stuff empirically before he did — "simple advertising costs least and sells most" (Kenneth Goode). But he calls out most copy for failing its own research: "most advertising copy nowadays is being written to satisfy the seller rather than the buyer" — i.e., optimized for what the brand wants to say, not for the reader's actual context and mood in the moment they encounter it. The ads he holds up as good examples (the Mr. Bambucci profile ad, the "I'm looking for a sergeant" story ad) work because they read like something a person would actually say, fitted to where the reader already is.

## Notable / Quotable

- "There is nothing more important to you as a speaker and writer than that your audience understand you; and on just this point you can never be sure." (Ch. I — the whole book exists because writers get no feedback loop, unlike a conversation partner's confused face.)
- "Use verbs. Let me repeat that: use verbs." (Ch. VIII)
- "Two short sentences are easier to understand than one long one, with extra stuff in it." (Ch. IX)
- "Most advertising copy nowadays is being written to satisfy the seller rather than the buyer." (Ch. XVIII)
- "It's like cooking vegetables and throwing away the water with all the vitamins in it" — on turning active verbs into passive/nominalized forms. (Ch. VIII)

## How This Applies to Emmanuel's Outreach/Sales Writing

Emmanuel's core revenue channel is [[cold-outreach]] — cold emails, proposals, and call scripts to US/UK/AU/CA business owners who are skimming, not studying. Flesch's framework maps directly onto that:

- **Cold email subject lines and opening lines** are exactly the "audience who can't talk back" problem Flesch opens the book with — no frown, no puzzled look, just a delete. The yardstick discipline (short sentences, root words, put people in the sentence) is a fast self-check before sending: does this read like something said to a person, or like sanitized business-speak?
- **The empty-words hit list is a direct edit pass for proposals** — Emmanuel's proposal/email drafts likely lean toward "in order to," "with regard to," "for the purpose of" when trying to sound professional. Flesch's point is that this reads as more distant, not more credible — it works against [[specificity-as-credibility]], the existing brand principle that concreteness (not formality) signals competence.
- **Live words over passive voice** matters most in the value-proposition line of a pitch: "we build the system that removes X" lands harder than "a system is built that removes X." This is a one-line self-check for `/write-email` and `/write-proposal` output.
- **The commenting-adjective rule** is a warning against stacking qualifiers onto a pitch line ("a fast, reliable, AI-powered, fully custom automation system") — Flesch's advice is to cut it to one plain sentence and let a second sentence carry the next claim, rather than crowding one sentence with unearned adjectives.
- **The "What Price Copy?" chapter is the most directly relevant chapter in the book** — its diagnosis that most copy serves the seller's ego rather than the buyer's actual moment applies one-to-one to cold outreach: the ask isn't "sound impressive," it's "fit the exact context and problem the prospect is already sitting in," which is also the substance behind [[pain-before-pitch]].

**Appears in:** [[identity]] · [[cold-outreach]]
**Related concepts:** [[specificity-as-credibility]] · [[pain-before-pitch]]
