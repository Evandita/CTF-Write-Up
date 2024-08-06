# Problem

## Description

楣瑦筴栴瑟楳渷彣桩渳獥

## Attachments

https://cybersharing.net/s/e964ad1143538987

# Solution

We don't actually need to look at the attachments for this because the description already give us the text that we needed to examine. To fulfill my curiosity, I decided to translate it to english and see what we get, turns out it means nothing.

Next, let's try to decode it using an online chinese to Unocide encoder and see what we get

```
\u6963\u7466\u7b74\u6834\u745f\u6973\u6e37\u5f63\u6869\u6e33\u7365
```

If we take a look at the result, this looks familiar to hexadecimal value for certain ascii. Let's try that.

```
ictf{th4t_isn7_chin3se
```

We got the flag, but it looks incomplete. Turns out just adding "}" will solve it. So, the flag is

**ictf{th4t_isn7_chin3se}**