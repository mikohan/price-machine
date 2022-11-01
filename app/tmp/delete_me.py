[
    {"name": "Delivered-To", "value": "suply.angara77@gmail.com"},
    {
        "name": "Received",
        "value": "by 2002:a59:c0aa:0:b0:30e:b472:1d71 with SMTP id f10csp4155304vqq;        Mon, 31 Oct 2022 21:22:49 -0700 (PDT)",
    },
    {
        "name": "X-Google-Smtp-Source",
        "value": "AMsMyM5osYX08tOu5dHQ8oaHMdN/TyItUouqOZpODhvDD+Ioig2tQHQp6YMBcSYykMJu90KYdMR3",
    },
    {
        "name": "X-Received",
        "value": "by 2002:a05:6512:314a:b0:4aa:2381:6fde with SMTP id s10-20020a056512314a00b004aa23816fdemr7098358lfi.36.1667276568534;        Mon, 31 Oct 2022 21:22:48 -0700 (PDT)",
    },
    {
        "name": "ARC-Seal",
        "value": "i=1; a=rsa-sha256; t=1667276568; cv=none;        d=google.com; s=arc-20160816;        b=EQFITg7XEpdZ5gOtDgOe0vysPQUVcgHuFLjusmWX9+FFCGCMgoVAGK39g6D13wHb2A         ODr4e1m8EjsAII26LXz+uSUzsr41XjX6i3qn/7BlQhU2Y3+6gOpFls2kuuUmN1KI0PeQ         DwmKsb00ahrJ9+NGXVj9Fvi8JX6pw8clJtQr48FouecvGiHVmfCZ23iU/u5+bHlgsAv/         Z+3fmRQ2QvXThA3Jay0USnf2FQd9n88Kdt81xeXkfkYFMGaVdXi6YogiHzxgGqQGBT2I         43o4l+0z/jH0JVgsh1a//aO7w6Ao0ruhWQT83JyCe60VuV+7C19xmH/nx6zblQ7PxGfu         2pvw==",
    },
    {
        "name": "ARC-Message-Signature",
        "value": "i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;        h=mime-version:message-id:to:subject:from:date:dkim-signature;        bh=ueXh5xrwWfTzqisza4MRXQH9VVdgVvjNuKK+BkASSzM=;        b=KjuSd3ojBlPxCrUQmrYi00J1G3qXfACC7hEu046WYgydkWHQYTV6EAX1FeQk82iCl+         7OBW2ClWVlMrCe79oH9wv0W7M/UgPamsYXCCMNqfSBY4gdYSB/49/LrSLEGq11Cv8O99         WCaqTOrYRV0opCZFGlCrO4JP85NHS8KiyfZSxdht36zWfJI50YQ9Kjxgz90U3V5E5gxf         SpwGBEZLweCehmb9EXOwhBRnpWARuxDSkAS7Ehcm49Iw+/TxO3NhO22UXb+HfoIvqB+r         9ueBpelzeJ7jyCl3qvaxUcQ+biit3f4d3BDsWhkajetP17beeORRscZlTRnHNA5JgJYr         lxQg==",
    },
    {
        "name": "ARC-Authentication-Results",
        "value": "i=1; mx.google.com;       dkim=pass header.i=@tokus77.ru header.s=mail header.b=XmKdgnk7;       spf=pass (google.com: domain of a.demich@tokus77.ru designates 37.140.190.203 as permitted sender) smtp.mailfrom=a.demich@tokus77.ru",
    },
    {"name": "Return-Path", "value": "<a.demich@tokus77.ru>"},
    {
        "name": "Received",
        "value": "from forward501o.mail.yandex.net (forward501o.mail.yandex.net. [37.140.190.203])        by mx.google.com with ESMTPS id r10-20020a2e80ca000000b00276aab0c8fdsi5556811ljg.376.2022.10.31.21.22.47        for <suply.angara77@gmail.com>        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-GCM-SHA256 bits=128/128);        Mon, 31 Oct 2022 21:22:48 -0700 (PDT)",
    },
    {
        "name": "Received-SPF",
        "value": "pass (google.com: domain of a.demich@tokus77.ru designates 37.140.190.203 as permitted sender) client-ip=37.140.190.203;",
    },
    {
        "name": "Authentication-Results",
        "value": "mx.google.com;       dkim=pass header.i=@tokus77.ru header.s=mail header.b=XmKdgnk7;       spf=pass (google.com: domain of a.demich@tokus77.ru designates 37.140.190.203 as permitted sender) smtp.mailfrom=a.demich@tokus77.ru",
    },
    {
        "name": "Received",
        "value": "from vla1-ef285479e348.qloud-c.yandex.net (vla1-ef285479e348.qloud-c.yandex.net [IPv6:2a02:6b8:c0d:35a1:0:640:ef28:5479]) by forward501o.mail.yandex.net (Yandex) with ESMTP id C17A545C3F5D for <suply.angara77@gmail.com>; Tue,  1 Nov 2022 07:21:40 +0300 (MSK)",
    },
    {
        "name": "Received",
        "value": "by vla1-ef285479e348.qloud-c.yandex.net (smtp/Yandex) with ESMTPSA id jZGAWfJFFd-Leg0aUHv; Tue, 01 Nov 2022 07:21:40 +0300",
    },
    {"name": "X-Yandex-Fwd", "value": "1"},
    {
        "name": "DKIM-Signature",
        "value": "v=1; a=rsa-sha256; c=relaxed/relaxed; d=tokus77.ru; s=mail; t=1667276500; bh=ueXh5xrwWfTzqisza4MRXQH9VVdgVvjNuKK+BkASSzM=; h=Message-Id:To:Subject:From:Date; b=XmKdgnk7rYfzszi49E+lRP3a4X2c8NIgqPF+U63GbClIGO6PV12IuPiIPVu10H2fL\t LUCkeWvBiVschM7omD0CrFB5Qw17SEpX0zA9dBOLvjYpG9RQKLFeVSDwGYbhmkv0Tx\t 2a06uZB8QN7ApgZckRkG7baGsFVbTH5Vaq5rC+MQ=",
    },
    {
        "name": "Authentication-Results",
        "value": "vla1-ef285479e348.qloud-c.yandex.net; dkim=pass header.i=@tokus77.ru",
    },
    {"name": "Date", "value": "Tue, 1 Nov 2022 07:21:40 +0300"},
    {"name": "From", "value": '"ООО \\"ТД Токус\\"" <a.demich@tokus77.ru>'},
    {"name": "Subject", "value": "Прайс-лист"},
    {"name": "To", "value": "<suply.angara77@gmail.com>"},
    {"name": "Message-Id", "value": "<753e8b3b-1f8b-43ce-b16e-d1b961bef4ae@gmail.com>"},
    {"name": "Mime-Version", "value": "1.0"},
    {"name": "X-Priority", "value": "3 (Normal)"},
    {"name": "X-Mailer", "value": "1C:Enterprise 8.3"},
    {
        "name": "Content-Type",
        "value": 'multipart/mixed; boundary="------_13764_1134043998_8040"',
    },
]
[
    {"name": "Delivered-To", "value": "suply.angara77@gmail.com"},
    {
        "name": "Received",
        "value": "by 2002:a59:c0aa:0:b0:30e:b472:1d71 with SMTP id f10csp3293297vqq;        Sun, 30 Oct 2022 22:02:25 -0700 (PDT)",
    },
    {
        "name": "X-Google-Smtp-Source",
        "value": "AMsMyM7lOGDP177cBPDt7O4EM9NqiWV1JGQ90Hem7v/iOL2qw9SxVI4UxKxTPrS7iP+h/dauoJ1T",
    },
    {
        "name": "X-Received",
        "value": "by 2002:a19:f70e:0:b0:4af:e7d3:5b5e with SMTP id z14-20020a19f70e000000b004afe7d35b5emr4360422lfe.339.1667192544754;        Sun, 30 Oct 2022 22:02:24 -0700 (PDT)",
    },
    {
        "name": "ARC-Seal",
        "value": "i=1; a=rsa-sha256; t=1667192544; cv=none;        d=google.com; s=arc-20160816;        b=hQh92btNlYnnRAvpInt0iTwq3balKRF13YX8pJr4siKSpJXkQdR9oPJRoqlPVpqhOc         3OTLJMGA+er4WEopTbTUP7ftLAGsGdnVRvssGR/HgYucETDNCjkPD5toLuf95VneSJKn         UpqUekzP7a4Q16jfuveRJvw01nh5Y5aEj/yyv6s5HhYqkVZCidTVzFw+daMB0sFHT6PJ         MBrIz0zkH5vv7qS1+uL+ari2U0QmU7xvU2DPcyaEJoXByLhthqSD9iAmpig7Dxa/dEtD         Y7HIBcfTSscA/F+dZSuNqyRyvvhSVQ6c/fQszRYiiY7zA3ble5JU9yL2iDEMesTz6VSY         JQoA==",
    },
    {
        "name": "ARC-Message-Signature",
        "value": "i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;        h=mime-version:message-id:to:subject:from:date:dkim-signature;        bh=k0CUnl1ZxhAb39f0xmOr6aL5ujCEY/ekyy3gTKTY62M=;        b=f0aCJwUyZqbUk691kaR3JNZ5kKsQDvaahl1LEmaVzxADR59vEbgnvGiVex0d2AzOFW         G0VbibImw6QVUmEF8itaZpA3XPC6as0hkcouVd/1+9w1sWjwTWvNGl+OHwb+fHtXVdoK         VSAVJb7ZGC1vpIsVLvI90eFI04Wf7PM3S8rmA83ITI7PJPA/DwFuZRPmaJG3v5nLlz6m         EMM+LB/scoIYFX8vMx6LSyeZAv2xuluOMQkn1Qcubca/wdG717zWSTfl42kd1Kf7daYL         j+On2zuIQfUeJeNkYsEuizdx1CgNYo7J0L2vvrZFC248KJineMZ9YA+r2ifjzJ899Rbj         cl6Q==",
    },
    {
        "name": "ARC-Authentication-Results",
        "value": 'i=1; mx.google.com;       dkim=pass header.i=@tokus77.ru header.s=mail header.b="W/zHOI3+";       spf=pass (google.com: domain of a.demich@tokus77.ru designates 77.88.28.113 as permitted sender) smtp.mailfrom=a.demich@tokus77.ru',
    },
    {"name": "Return-Path", "value": "<a.demich@tokus77.ru>"},
    {
        "name": "Received",
        "value": "from forward503p.mail.yandex.net (forward503p.mail.yandex.net. [77.88.28.113])        by mx.google.com with ESMTPS id f10-20020a0565123b0a00b004aada4e8b88si4072394lfv.65.2022.10.30.22.02.24        for <suply.angara77@gmail.com>        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-GCM-SHA256 bits=128/128);        Sun, 30 Oct 2022 22:02:24 -0700 (PDT)",
    },
    {
        "name": "Received-SPF",
        "value": "pass (google.com: domain of a.demich@tokus77.ru designates 77.88.28.113 as permitted sender) client-ip=77.88.28.113;",
    },
    {
        "name": "Authentication-Results",
        "value": 'mx.google.com;       dkim=pass header.i=@tokus77.ru header.s=mail header.b="W/zHOI3+";       spf=pass (google.com: domain of a.demich@tokus77.ru designates 77.88.28.113 as permitted sender) smtp.mailfrom=a.demich@tokus77.ru',
    },
    {
        "name": "Received",
        "value": "from vla1-62318bfe5573.qloud-c.yandex.net (vla1-62318bfe5573.qloud-c.yandex.net [IPv6:2a02:6b8:c0d:3819:0:640:6231:8bfe]) by forward503p.mail.yandex.net (Yandex) with ESMTP id 2AF4F1100EA7 for <suply.angara77@gmail.com>; Mon, 31 Oct 2022 08:02:24 +0300 (MSK)",
    },
    {
        "name": "Received",
        "value": "by vla1-62318bfe5573.qloud-c.yandex.net (smtp/Yandex) with ESMTPSA id MwQ7pz8XFV-2NgWElqA; Mon, 31 Oct 2022 08:02:23 +0300",
    },
    {"name": "X-Yandex-Fwd", "value": "1"},
    {
        "name": "DKIM-Signature",
        "value": "v=1; a=rsa-sha256; c=relaxed/relaxed; d=tokus77.ru; s=mail; t=1667192543; bh=k0CUnl1ZxhAb39f0xmOr6aL5ujCEY/ekyy3gTKTY62M=; h=Message-Id:To:Subject:From:Date; b=W/zHOI3+KGDL3S0SX+e9KdFvxoY1C+m6w08ECS8hAzn1vKJOfFP598ZPP3ZFVUBGs\t 26VVq94Rvnb4cExoLiMVbMuo+C4GRUML6YNSsA+6MyfikR5ZMZfP72NIkEbm+qq+9i\t +rRCzfkriUNLRp3mpd23tjpuYPiVnRwBsCiotBEA=",
    },
    {
        "name": "Authentication-Results",
        "value": "vla1-62318bfe5573.qloud-c.yandex.net; dkim=pass header.i=@tokus77.ru",
    },
    {"name": "Date", "value": "Mon, 31 Oct 2022 08:02:23 +0300"},
    {"name": "From", "value": '"ООО \\"ТД Токус\\"" <a.demich@tokus77.ru>'},
    {"name": "Subject", "value": "Прайс-лист"},
    {"name": "To", "value": "<suply.angara77@gmail.com>"},
    {"name": "Message-Id", "value": "<4db22688-2e9c-4fd3-a2cc-d6b54c58a9c3@gmail.com>"},
    {"name": "Mime-Version", "value": "1.0"},
    {"name": "X-Priority", "value": "3 (Normal)"},
    {"name": "X-Mailer", "value": "1C:Enterprise 8.3"},
    {
        "name": "Content-Type",
        "value": 'multipart/mixed; boundary="------_26804_1050095889_8040"',
    },
]
[
    {"name": "Delivered-To", "value": "suply.angara77@gmail.com"},
    {
        "name": "Received",
        "value": "by 2002:a59:c0aa:0:b0:30e:b472:1d71 with SMTP id f10csp1035200vqq;        Thu, 27 Oct 2022 21:51:55 -0700 (PDT)",
    },
    {
        "name": "X-Google-Smtp-Source",
        "value": "AMsMyM5fqQOjNp8Ssxvk2rzMxwXx07nUZFzaoZ+tTBHwNxKUlYyYKnwCnS4VpAbBhVqZCbcD+K6A",
    },
    {
        "name": "X-Received",
        "value": "by 2002:a05:651c:983:b0:26c:1c6b:8473 with SMTP id b3-20020a05651c098300b0026c1c6b8473mr18564436ljq.341.1666932714687;        Thu, 27 Oct 2022 21:51:54 -0700 (PDT)",
    },
    {
        "name": "ARC-Seal",
        "value": "i=1; a=rsa-sha256; t=1666932714; cv=none;        d=google.com; s=arc-20160816;        b=J4euZCDvhKhoUILsEZsN7F8FMwWPr0rhZmj2suZxd2vGAoHjClgy8cV6tPTsKGWujE         j/5ofb4X2XaYwNLKF42bBcVbO41YTQaq/azOPySo67y57bQhA5VyrLueYzmOLNwL2lhw         sCTLPnevpb+FsCaJH8hsfgSkzMeOmR3uugAvdd+2GXZSjTlFnFdsP0HHV7T8J8t0R5ZV         AUI0ePE9QjtzgqZLFrFX51MgnRYXwckLuQ4VkAoNWD39SPwUTigTkDTBq+x/AwrYJ61p         lSQms9U61ZZs23E6LxQ9KVSDZA0cDw22VbQ84oFyta6nNoiY8daZ9rACwf/b7Rwflqm8         jp9Q==",
    },
    {
        "name": "ARC-Message-Signature",
        "value": "i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;        h=mime-version:message-id:to:subject:from:date:dkim-signature;        bh=aJ09jOEslakbW/k4Tbk9xZf6d9on/LAQpZmCjZy7qhY=;        b=pQjLJzKtdf6kAr4zO8ocTV34TLRsddKo3awNERZmNPEyQvIv1VdwTReg/biUZBKOt3         fnvOZiyYRwii9uDtLFyTAIdwWIZj0F2WN6IQ7Y8ID+eYOC4NV3ouX6eMPpnyEnjNazV9         LwwG+EaSZPYw60Bzqsu/OdnUnhNZS1vhuUfU1CI+dlnDSLv6+rbaxZpiHpvmc/Ltxct7         JrYlnNusic9r6sUhWbb2ppfyPWOrVIhficpUG4PPw1myw+YP9PhX/lG/IXGHZQdT63qi         oE89a8lfyZ0xu2CzeHwF2fAkGPxTYrDqqLpo9Wy2vUhGlfacyLHBypr9RF9Y91jXFtXy         y6Pw==",
    },
    {
        "name": "ARC-Authentication-Results",
        "value": "i=1; mx.google.com;       dkim=pass header.i=@tokus77.ru header.s=mail header.b=A3DYAzwL;       spf=pass (google.com: domain of a.demich@tokus77.ru designates 5.45.198.250 as permitted sender) smtp.mailfrom=a.demich@tokus77.ru",
    },
    {"name": "Return-Path", "value": "<a.demich@tokus77.ru>"},
    {
        "name": "Received",
        "value": "from forward500j.mail.yandex.net (forward500j.mail.yandex.net. [5.45.198.250])        by mx.google.com with ESMTPS id u8-20020a056512128800b00497aaa8311esi2183132lfs.317.2022.10.27.21.51.54        for <suply.angara77@gmail.com>        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-GCM-SHA256 bits=128/128);        Thu, 27 Oct 2022 21:51:54 -0700 (PDT)",
    },
    {
        "name": "Received-SPF",
        "value": "pass (google.com: domain of a.demich@tokus77.ru designates 5.45.198.250 as permitted sender) client-ip=5.45.198.250;",
    },
    {
        "name": "Authentication-Results",
        "value": "mx.google.com;       dkim=pass header.i=@tokus77.ru header.s=mail header.b=A3DYAzwL;       spf=pass (google.com: domain of a.demich@tokus77.ru designates 5.45.198.250 as permitted sender) smtp.mailfrom=a.demich@tokus77.ru",
    },
    {
        "name": "Received",
        "value": "from sas2-cc22fd2335f8.qloud-c.yandex.net (sas2-cc22fd2335f8.qloud-c.yandex.net [IPv6:2a02:6b8:c08:6c82:0:640:cc22:fd23]) by forward500j.mail.yandex.net (Yandex) with ESMTP id D9F6A6CB6469 for <suply.angara77@gmail.com>; Fri, 28 Oct 2022 07:51:53 +0300 (MSK)",
    },
    {
        "name": "Received",
        "value": "by sas2-cc22fd2335f8.qloud-c.yandex.net (smtp/Yandex) with ESMTPSA id OLk7LF4Jp2-prgiBOI9; Fri, 28 Oct 2022 07:51:53 +0300",
    },
    {"name": "X-Yandex-Fwd", "value": "1"},
    {
        "name": "DKIM-Signature",
        "value": "v=1; a=rsa-sha256; c=relaxed/relaxed; d=tokus77.ru; s=mail; t=1666932713; bh=aJ09jOEslakbW/k4Tbk9xZf6d9on/LAQpZmCjZy7qhY=; h=Message-Id:To:Subject:From:Date; b=A3DYAzwL1tQTXnV4gMeIzUwA0eujKaL/rkNccCTLGJrFGvQix608btJrX8Cl43pF7\t ywayCLmcaHShspLceTkuSttyW1YtGqMcVSh0nDgXmeiw9WSZQrip4uvsXJPLGCpw6o\t JW6HBycYo4c37iEwjeDoqsGPNldGHfFCIXGEFfl8=",
    },
    {
        "name": "Authentication-Results",
        "value": "sas2-cc22fd2335f8.qloud-c.yandex.net; dkim=pass header.i=@tokus77.ru",
    },
    {"name": "Date", "value": "Fri, 28 Oct 2022 07:51:52 +0300"},
    {"name": "From", "value": '"ООО \\"ТД Токус\\"" <a.demich@tokus77.ru>'},
    {"name": "Subject", "value": "Прайс-лист"},
    {"name": "To", "value": "<suply.angara77@gmail.com>"},
    {"name": "Message-Id", "value": "<f79cef60-70da-4439-8f52-0bd171d2f665@gmail.com>"},
    {"name": "Mime-Version", "value": "1.0"},
    {"name": "X-Priority", "value": "3 (Normal)"},
    {"name": "X-Mailer", "value": "1C:Enterprise 8.3"},
    {
        "name": "Content-Type",
        "value": 'multipart/mixed; boundary="------_23388_790291748_8040"',
    },
]
