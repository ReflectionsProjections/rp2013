---
layout: speaker
name: Brandon Wiley
photo_url: /images/speakers/placeholder.jpg
category: speakers
one_line: "PhD Candidate, Information Studies<br />University of Texas at Austin"
---
# Defeating Protocol Classifying Internet Filters with Dust, the Polymorphic Protocol Engine
A widely deployed method of filtering Internet traffic is by using protocol fingerprinting, a specific form of what is generally know as "Deep Packet Inspection". Protocols such as SSL, Tor, BitTorrent, and VPNs are being summarily blocked, regardless of their specific uses. It is possible to circumvent this filtering by encoding traffic into a form which cannot be correctly fingerprinted by the filtering hardware. I will be presenting a tool called Dust which provides an engine for encoding traffic into a variety of forms. By developing a good model of how filtering hardware differentiates traffic into different protocols, a profile can be created which allows Dust to encode arbitrary traffic to bypass the filters.

Dust is different than other approaches because it is not simply another protocol designed to be hard to detect. It is an engine which can encode traffic according to the given specifications. As the filters change their algorithms for protocol detection, rather than developing a new protocol, Dust can just be reconfigured to use different parameters. In fact, Dust can be automatically reconfigured using examples of what traffic is blocked and what traffic gets through. Using machine learning a new profile is created which will encode traffic so that it resembles that which gets through and not that which is blocked. Dust has been created with the goal of defeating real filtering hardware currently deployed for filtering Internet traffic. In this talk I will discuss how the real filtering hardware works and how to effectively defeat it.


## About Brandon
Brandon Wiley is a peer-to-peer pioneer who creates tools to circumvent Internet censorship. In 1999 he co-founded the Freenet project to create a censorship-resistant publishing platform. He is also known for the Curious Yellow superworm design. When working for BitTorrent, Inc. he was given the difficult task of trying to reason with the Internet service providers that were engaging in BitTorrent throttling. More recently he has been working for the Tor project on their next generation blocking-resistant protocol systems such as obfsproxy and obfs3. He is currently a PhD candidate in Information Studies at the University of Texas at Austin, where he is studying all of the most popular Deep Packet Inspection hardware and figuring out how to defeat it.
