---
title: "Grids Worldwide Sag Every Sixty Seconds, and Researchers Traced It to Data Centre Battery Self-Checks"
title_en: "Grids Worldwide Sag Every Sixty Seconds, and Researchers Traced It to Data Centre Battery Self-Checks"
date: "2026-11-09T05:02:36+08:00"
draft: "false"
tier: "1"
description: "Researchers at Germany's Forschungszentrum Juelich, working with transmission system operator Tennet Germany, have explained a frequency sag that appears every sixty seconds on grids in Europe, Australia, the United States and Malaysia: large numbers of internet-connected stationary batteries check their state of charge on the same minute. The team reproduced the effect locally using more than 80 smart power quality meters on a research campus. On Ireland's grid, where data centres reached 18 per cent of load by 2022, the minute-by-minute drop rose from 3 milli-Hertz in 2016 to 12 milli-Hertz in 2021 and has recently passed 20 milli-Hertz."
summary: "The finding identifies a class of infrastructure risk that has no single point of failure: a large population of networked devices, all checking their own state on the same clock tick."
source: "TechCrunch"
categories:
  - "science"
tags:
  - "Power Grid"
  - "Data Centres"
  - "Uninterruptible Power Supply"
  - "Energy Storage"
  - "Power Quality"
  - "Energy Transition"
---

## Key Facts

For years, electricity grids in Europe, Australia, the United States and Malaysia have shown a small frequency sag at precisely sixty-second intervals, occurring at the same moment across continents. A research team at Germany's Forschungszentrum Juelich, working with transmission system operator Tennet Germany, has identified the cause: large numbers of internet-connected stationary batteries, from data centre uninterruptible power supplies to grid-scale storage, check their state of charge on the same minute, and their synchronised checks accumulate into a measurable disturbance on the wide grid. On Ireland's grid, where data centres accounted for 18 per cent of electricity demand by 2022, the minute-by-minute frequency drop quadrupled from 3 milli-Hertz in 2016 to 12 milli-Hertz in 2021, and has recently exceeded 20 milli-Hertz.

## Event Details

- **The pattern**: frequency on the grid drops by a small amount every 60 seconds, and the sags occur at exactly the same time on grids in different countries and continents.
- **Why it matters**: grid operators rely on frequency staying within a defined band; large oscillations or an improper response can lead to blackouts, and even sub-blackout sags can damage equipment such as hydropower turbines if left unchecked.
- **The first hypothesis**: hydropower turbines vibrate at a resonant frequency, which can magnify under the right conditions, much as a wine glass can shatter under a sustained high note. The team modelled a hydropower plant control system on the Scandinavian grid and did find conditions producing a resonance peaking once per minute, but could not explain its persistence, since mechanical resonances normally decay.
- **The insight**: the researchers reasoned that anything operating with such clockwork regularity must require a clock.
- **The measurement**: more than 80 smart power quality meters were installed around the Juelich campus, covering medium- and low-voltage distribution lines, transformers, solar panels and battery energy storage systems, sampling frequency, voltage, current and power once every three seconds.
- **The finding**: the transformer attached to the battery energy storage system peaked every minute, matching the pattern seen on larger grids.
- **The mechanism**: many stationary batteries check their state of charge every minute; because these devices are internet-connected their clocks stay in near-perfect synchronisation, and while a single check is imperceptible on a wide grid, the collective effect is not.
- **The Irish case**: with data centres consuming 18 per cent of national grid load by 2022 and each facility served by a fleet of uninterruptible power supplies, the minute-by-minute drop on Ireland's grid quadrupled from 3 milli-Hertz in 2016 to 12 milli-Hertz in 2021, with some more recent drops above 20 milli-Hertz.
- **The margin**: Ireland's 50 Hertz grid is designed to withstand swings of plus or minus 200 milli-Hertz, though the operator would prefer to hold swings to 100 milli-Hertz; the problem is that data centres are not the only loads, so other sources of sag can compound with the battery effect.
- **The fix**: researchers recommend that uninterruptible power supply and grid-scale battery manufacturers randomise the schedule of state-of-charge checks rather than performing them exactly on the minute.

## Comparison of Viewpoints

**The research contribution is a change of attribution, and it earns credibility by reproducing the effect locally before extrapolating it globally.** The conventional explanation for ultra-low frequency oscillations pointed at hydropower resonance, a physically plausible mechanism but one that normally decays. The team's local replication, using 80 meters on a research campus with its own transformers, panels and storage, is what allowed them to observe the same one-minute peak that appears on intercontinental grids, and only then check that grid operator data showed the same signature. That ordering, controlled measurement first and statistical confirmation second, is what makes the conclusion difficult to dismiss.

**The grid operators' concern is about margin rather than about the absolute size of the disturbance.** Twenty milli-Hertz looks trivial against a design tolerance of 200 milli-Hertz. But the tolerance applies to the sum of all disturbances, and the point of the Ireland data is that this particular contributor grows with data centre density. Ireland, where data centres reached 18 per cent of load, is not a hypothetical case but a demonstration of how the effect scales, and the trajectory from 3 to 12 milli-Hertz in five years, with newer readings above 20, suggests the curve has not flattened.

**For manufacturers, the cost of the fix is close to zero, which is precisely what makes it hard to deliver.** Randomising a check schedule requires a firmware change and nothing else. The difficulty is structural: the fix only pays off if a large fraction of the installed base does it, because the disturbance emerges from aggregate synchrony, and no individual operator gains anything from being first. This is a textbook collective action problem sitting inside a supply chain with many vendors and millions of units already installed.

**The framing from the research side is notably free of alarm.** The team presented the issue as entirely preventable rather than as a security concern, and the substance of the recommendation is a scheduling change rather than a hardware revision. That restraint matters for how the finding is likely to be received by utilities that are simultaneously being asked to accommodate rapid data centre growth, since a finding framed as a shared systems problem invites cooperation where one framed as a threat invites litigation.

**One caveat deserves attention.** The mechanism explains the timing and the signature cleanly, but the contribution of the battery effect to any particular grid's total frequency variability is a question of decomposition. Other loads cause their own sag, and the researchers are explicit that the additional push from synchronised battery checks matters precisely because other contributions are already present. The finding identifies a contributor that is newly measurable and newly controllable, rather than a complete accounting of grid variability.

## Panoramic Analysis

What this research exposes is a category of infrastructure risk that did not exist before the current build-out of compute: not equipment failure, not malicious action, but the collective behaviour of a large population of networked devices whose clocks are aligned. Traditional grid loads are driven by human schedules and industrial rhythms, and are therefore naturally noisy. A stationary battery management system is different in kind. It is software-driven, network-connected, time-synchronised, and it runs a periodic self-check at a fixed interval. Each of those four properties is a design decision that makes the device better at what it does. Together they make the fleet behave like one device rather than many.

The irony is that the offending behaviour is a feature of reliability. Checking state of charge on a schedule is how the operator knows the system is healthy, and the failure mode of removing it would be worse. So the finding cannot be resolved by asking operators to check less often, and it cannot be resolved by making the checks irregular in an arbitrary way, because irregularity is precisely the property being recommended. The fix is to randomise the schedule so that no instant is synchronised across the fleet, which preserves every safety property of periodic checking while removing the shared phase relationship. It is a change of one variable in one software routine, and it is the kind of change that could have been made years ago if anyone had known to look.

The timing is notable. The conversation about compute and electricity has been dominated by supply and queueing: how many gigawatts are needed, how long an interconnection takes, what to do about multi-year waits. This finding points at a different constraint operating in a completely different register, one about the quality of the power rather than the quantity, and it affects the operator's ability to absorb large new loads without degrading service to existing ones. For data centre siting decisions, that suggests a category of assessment that does not currently exist in most proposals: not how much power the site can secure, but how many time-synchronised storage devices operate within the same balancing region.

The most likely path to a fix is dull, which is why it is worth stating plainly. The chain runs from research finding, to operator observation, to a specification in procurement requirements, to a firmware default. The first two steps are already done. The third is where the outcome is actually decided, and it is decided by a small number of procurement staff who will not be in the room when the question of attribution comes up. If that step fails, the effect persists in the grid long after attention has moved elsewhere, because the installed base has a long replacement cycle and nothing forces a change during it. The cheapest technical fix in this story is therefore also the one most dependent on someone writing it into a contract.



Editor: GoodInfo Global News Team
