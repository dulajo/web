---
name: smart-home
description: A smart home that saves time instead of adding worries. Lights, blinds, heating and appliances finally talk to each other, and the house takes care of plenty on its own without you having to think about it. Have a smart home? We'll take a look, whatever it runs on. Don't have one? We'll talk through what would make sense for you. Use when you want a house that works reliably and predictably. Not for electrical installation work.
---

# Smart home

I'm a programmer, and we run our house on Loxone, extended with Home Assistant. Our home assistant has all the paperwork for the house, so we don't have to dig through papers, spreadsheets and emails. I'm happy to look at yours too.

## When I can help

- You have a smart home, but your devices talk to each other like neighbours over a fence
- You don't have a smart home yet, but you'd like one and want to talk through the options
- You are building or renovating and want to plan the smart home from the start
- You don't want to automate the whole house, but you'd like to automate at least the paperwork around it: warranties, insurance, servicing
- You want your own home server (homelab) and your data at home, not "somewhere in the cloud"
- You want a home AI assistant that answers from your own records, not off the top of its head

## What you need

- Nothing in particular. You don't need Loxone, Home Assistant or your own server, or you can have all of them and something else besides. Further down is just how we do it.
- A home assistant can run at several levels. The simplest is an app on your computer that runs only when you switch it on. One step further is a separate, even older computer that runs around the clock and sees only what you allow. And furthest is home hardware powerful enough to run its own AI model: all the data stays at home and nothing goes to the cloud. Connecting the assistant to a smart home and its sensors works at any of these levels.
- You control what the assistant sees. Don't want it in your email? It gets its own mailbox and you forward only what it should see. Don't want to give it your whole Google Drive? It gets its own account and you share just the folders you choose.

## How I work

- First I understand what you need, then I suggest a solution that fits you. Not the one that's coolest right now.
- Automations should save time, and you should barely notice them. They shouldn't add worries or drive you mad.
- If AI is to run the house in any way or help with the paperwork, it needs clear rules and limits so you can rely on it.

## What runs at our place

- Loxone as the base: lights, blinds, ventilation with heat recovery, the heat pump and security
- Home Assistant for the rest: appliances, cameras and more complex automations on top of Loxone
- A homelab with a few home services that save us subscriptions to the big platforms, such as a password manager and a document manager
- The central brain of the house: all the paperwork in one place, neatly organised
- A home assistant that can work with any of these, depending on what we allow it
- The latest addition: a 3D model of the whole house. The AI model Astra redrew it from the house plans with the help of the free Blender, adds furniture from current photos, and we use it to fine-tune changes to the rooms.

## Examples

**Input:** The hot water circulation pump kept running even when nobody needed hot water.
**Output:** It's driven by a mix of presence, house mode and the cycle length actually needed. On top of that, the assistant checks it really runs only as much as it should, and speaks up when it doesn't. The analysis right below shows what that looks like.

**You:** Analyse the heat pump over the last month.
**Assistant:** The heat pump is fine; I found no faults in the last 30 days. The compressor runs long cycles with no short-cycling, and the seasonal performance factor for heating is 4.8. The savings are elsewhere: the night program heats to 22 °C while the day setting is only 21 °C, and the hot water circulation still runs about 1.5 hours a day. Fixing both, and trying to heat in the afternoon instead, could save roughly CZK 1,000–2,000 a year. I haven't changed anything.

**Input:** Finding a warranty card or a contract meant digging through drawers and folders.
**Output:** Documents live in our home document manager, and the assistant finds them in seconds.

**Assistant:** The heat pump service was due today. Did it happen? Do we have a report? If so, send it to me, along with the invoice for the work. Is there anything I should note that isn't in the report? Unless you say otherwise, I'll remind you in 11 months to book the next service.

**Assistant:** Today's agenda: book the ventilation unit service. There's a draft ready in your email, check it and send it.

It could book the service on its own, but for now we want to have the last word.

## Not a fit

- Electrical installation. I'm a programmer and solution architect, not an electrician.

## Get in touch

Is something at home not working the way you'd like, or are you only just thinking about a smart home? Tell me what you're dealing with, and we'll see whether and how I can help.

- Email: dulajosef@gmail.com
- LinkedIn: [linkedin.com/in/josef-dula-530505b3](https://www.linkedin.com/in/josef-dula-530505b3)
