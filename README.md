# Neurosity Python SDK 🤯

Welcome to the official Neurosity Python SDK. This library is compatible with Python 3.

## Documentation

- [Getting Started](#getting-started)
- [Authentication](#authentication)
- [Brainwaves](#brainwaves)
- [Signal Quality](#signal-quality)
- [Accelerometer](#accelerometer)
- [Calm](#calm)
- [Focus](#focus)
- [Kinesis](#kinesis)
- [Device Info](#device-info)
- [Device Status](#device-status)
- [Device Settings](#device-settings)

## Getting Started

To get started with the Neurosity SDK, you'll need:

- Your device ID
- Your Neurosity account email
- Your Neurosity account password

To get your 32-character Neurosity device ID, use the Neurosity mobile app available for iOS and Android. Go to `Settings -> Device Info`.

> 💡 Never hardcode your email and password directly in your Python code. Instead, create a `.env` file in the root of your project and add:

```bash
NEUROSITY_EMAIL=your email here
NEUROSITY_PASSWORD=your password here
NEUROSITY_DEVICE_ID=your device id here

```

## Authentication

We take data privacy very seriously at Neurosity. This is why we have designed the Neurosity OS to require authentication and authorization for streaming data.

When you sign up for an account on the Neurosity mobile app or console.neurosity.co and claim a device you have three new important items: deviceId, email, and password. If your device is not added to your Neurosity account, you will not be able to authenticate with it.

```python
from neurosity import NeurositySDK
from dotenv import load_dotenv
import os

load_dotenv()

neurosity = NeurositySDK({
    "device_id": os.getenv("NEUROSITY_DEVICE_ID"),
})

neurosity.login({
    "email": os.getenv("NEUROSITY_EMAIL"),
    "password": os.getenv("NEUROSITY_PASSWORD")
})
```

## Brainwaves

The brainwaves API is what we always wished for when it came to inventing the future: an easy way to get lossless brainwaves. Sometimes we wanted to manipulate the raw data and other times we wanted to analyze the power in each frequency bin. With brainwaves, our goal is to enable new APIs and powerful programs to be built. We expect that someone working with the brainwaves API has a bit of experience working with EEG data or a strong desire to learn.

### Sampling Rate

The sampling rate will vary depending on the model of your device.

- Crown -> 256Hz
- Notion 2 -> 250Hz
- Notion 1 -> 250Hz

A sampling rate of 250Hz means the data contains 250 samples per second.

### Metrics

There are four brainwaves metrics:

- raw
- rawUnfiltered
- psd
- powerByBand

### Raw

The `raw` brainwaves parameter emits events of 16 samples for Crown and 25 for Notion 1 and 2. We call these groups of samples Epochs.

```python
from neurosity import NeurositySDK
from dotenv import load_dotenv
import os

load_dotenv()

neurosity = NeurositySDK({
    "device_id": os.getenv("NEUROSITY_DEVICE_ID"),
})

neurosity.login({
    "email": os.getenv("NEUROSITY_EMAIL"),
    "password": os.getenv("NEUROSITY_PASSWORD")
})

def callback(data):
    print("data", data)

unsubscribe = neurosity.brainwaves_raw(callback)
```

The code above will output new epochs of 16 samples approximately every 62.5ms (see the `data` property). Here's an example of 1 event:

```
{
  label: 'raw',
  data: [
    [
        4.457080580994754,   4.851055413759571,
       2.7564288713972513, -0.5027899221971044,
       -2.738312652550817, -1.4222768509324195,
       3.7224881424127774,  10.026623768677425,
       13.387940036943913,   10.26958811063134,
      0.40214439930276313,  -10.90689891807639,
       -16.32031531728357,  -13.21110292437311,
       -4.346339152926361,   5.098462672115731
    ],
    [
       1.5414324608328491,   1.352550875105505,
       0.6428681224481866,  0.3647622839064659,
        1.106405158893898,    3.33535030106603,
        6.439447624257519,   8.453867322080404,
        7.755719477492251,  3.8854840128526726,
       -2.468418708869076,  -8.666576946507902,
      -11.279063910921169,   -9.32163910159064,
      -4.6549399985975555, 0.22830321396497988
    ],
    [
       6.2342484244030345,   5.845156697083605,
       3.8819440822537112,   1.452431055127227,
      -0.5878084105038387, -0.7746780077287738,
       1.8154316196085094,   6.074662974618359,
        9.322430831260775,   8.910160063433407,
       3.5874046672323043,  -4.554187036159066,
        -10.5813322711113, -11.267696723897789,
       -6.818338145262863,  0.6177864457464617
    ],
    [
      -0.03815349843983071, -0.3068494494059635,
       -2.2075671327003255,  -3.776991642244289,
        -3.708252867923816, -1.2505125622236009,
        3.2487010722502587,   7.931368090269462,
        10.511652358411597,   9.297157466389192,
         4.118487064147775,  -2.970255165231891,
        -8.603434324519576, -10.495401970387743,
        -8.913968355428027,  -5.576315727924461
    ],
    [
      0.4087987173450871, 1.9781686568610883,
      2.4009012312957907, 2.3444623435812657,
       2.017191526524595,  2.021880260660721,
       2.982232584662937,  4.815498699074363,
      6.7093290202119835,  7.201157697368587,
       5.116090777276677, 0.6675802498302112,
      -4.274751517565271, -7.425134286013973,
      -7.838523284654038, -5.779233789541195
    ],
    [
       5.2762700288652935,   6.831919893235682,
        6.468141714172544,   5.147606136919876,
        4.117592132996127,   4.788874365858218,
        7.116782027901927,    9.33554991116211,
        9.233167024756574,   5.130966403760715,
      -2.8162586562506586,  -11.22160733448037,
      -15.538132012307846, -13.939535958562475,
        -7.83032193319038, -0.5139467086717411
    ],
    [
      -1.0706877843314648,  1.6368537502872518,
        2.022946637839514,   0.940183871324582,
      -0.2837858448921892,  0.3170369574339986,
        3.778225479624427,   8.805770181583913,
       12.446309024446833,  11.648691354684154,
        5.113617281379798,  -4.345975093596486,
       -11.05811376487729, -11.719256256733335,
       -7.336025188705039,  -1.276174494743728
    ],
    [
        7.286685329938873,    8.201842402616839,
        5.517128178717949,   1.2864058791627557,
      -1.5101995538838966, -0.19819079250913285,
        5.195437241439434,   11.512563735679437,
       14.388370410845482,   10.711863367882668,
       0.8428177428317678,  -10.126402143316568,
       -15.75585412249734,  -13.887360795976967,
       -6.836657125920971,   1.1706118773123455
    ]
  ],
  info: {
    channelNames: [
      'CP3', 'C3',
      'F5',  'PO3',
      'PO4', 'F6',
      'C4',  'CP4'
    ],
    notchFrequency: '60Hz',
    samplingRate: 256,
    startTime: 1628194299499
  }
}
```

Epochs are pre-filtered on the device's Operating System to give you the cleanest data possible with maximum performance. These filters include:

- Notch of `50Hz` or `60Hz` and a bandwidth of `1`.
- Band Pass with cutoff between `2Hz` and `45Hz`.

The order of these filters is set to `2`, and the characteristic used is `butterworth`.

To apply your own filters, you can use the `brainwaves_raw_unfiltered` SDK method (see next section) and use a library like MNE or Brainflow for fine-grained filter customization.

#### Unsubscribe from brainwaves

To unsubscribe from brainwaves and stop the emission of data events, you can do the following:

```python
unsubscribe = neurosity.brainwaves_raw(callback)

timer.sleep(5)

unsubscribe()
```

This last example will emit data for 5 seconds.

### Raw Unfiltered

The unfiltered raw data follows the same shape as `brainwaves_raw` data shape, just without signal filters applied. This data comes directly from the analog to digital converter, and does not include any processing. We only recommend using the unfiltered data for advanced scenarios.

Note that unfiltered raw data will include environmental noise in the signal, as well as DC drift, which is expected when working with EEG.

```python
from neurosity import NeurositySDK
from dotenv import load_dotenv
import os

load_dotenv()

neurosity = NeurositySDK({
    "device_id": os.getenv("NEUROSITY_DEVICE_ID"),
})

neurosity.login({
    "email": os.getenv("NEUROSITY_EMAIL"),
    "password": os.getenv("NEUROSITY_PASSWORD")
})

def callback(data):
    print("data", data)

unsubscribe = neurosity.brainwaves_raw_unfiltered(callback)
```

The code above will output new epochs of 16 samples approximately every 62.5ms (see the `data` property).. Here's an example of 1 event:

```
{
  label: 'rawUnfiltered',
  data: [
    [
       1385.227003,   861.056247,
      -1835.167617, -1321.189256,
        999.860579,  1414.597195,
      -1246.623837, -1840.934367,
        406.757043,  1596.652153,
       -476.360375, -2080.790935,
       -222.556318,  1579.754234,
        355.660956, -2065.368232
    ],
    [
        774.21972,    286.25879,
      -951.714922,  -427.812387,
       650.368705,   611.744891,
      -746.391799,    -732.3102,
       398.039863,   770.732848,
       -412.99318,  -923.417614,
       122.174635,   823.840593,
         7.040799, -1004.286225
    ],
    [
       797.085555,   234.693316,
       -1099.4376,  -499.427375,
       669.613557,   598.870286,
      -859.916308,  -839.665628,
       420.369256,    765.63665,
      -515.185355,  -1057.66219,
       114.195062,   849.388636,
       -42.177742, -1155.495775
    ],
    [
       192.783795, -156.909245,
      -538.654687, -173.673053,
       210.084045,   13.008715,
      -496.208724, -314.354932,
       130.355373,  111.244632,
      -422.783244, -437.267174,
        43.116515,  179.573914,
      -267.952711, -512.234925
    ],
    [
       228.256013, -147.253292,
      -549.249414, -160.731394,
       234.961536,   16.093256,
      -506.803451, -304.162537,
       164.553542,   135.31746,
      -437.870671, -440.217605,
        71.212657,  207.267725,
       -272.04308, -523.634314
    ],
    [
        654.66024,   123.64985,
      -906.720861, -336.013773,
       578.217274,  426.337171,
      -751.487996, -629.246306,
       371.821267,  573.791629,
      -480.853076,  -827.26041,
       143.028812,  673.435705,
      -121.839358, -934.682893
    ],
    [
       764.362601,   258.095592,
      -996.172541,  -464.826875,
       639.975144,   603.094766,
      -765.368429,  -772.208063,
       384.829982,   745.453025,
       -437.46834,  -963.851919,
        93.139719,   807.747337,
       -22.865834, -1044.519364
    ],
    [
       1454.293893,   821.493659,
      -1599.334362,  -991.813951,
       1131.892333,  1364.506936,
      -1098.431772, -1494.459978,
        603.228876,  1578.815461,
        -421.71036, -1753.024956,
         21.860006,  1608.252708,
        343.859235, -1787.089015
    ]
  ],
  info: {
    channelNames: [
      'CP3', 'C3',
      'F5',  'PO3',
      'PO4', 'F6',
      'C4',  'CP4'
    ],
    samplingRate: 256,
    startTime: 1628194299499
  }
}
```

### Power Spectral Density (PSD)

```python
def callback(data):
    print("data", data)

unsubscribe = neurosity.brainwaves_psd(callback)
```

The code above will output new epochs 4 times a second. Every frequency label (e.g. alpha) contains the computed FFT (Fast Fourier transform) value per channel (see the `psd` property), as well as the frequency ranges (see the `freqs` property).

Here's an example of 1 event:

```
{
  label: 'psd',
  freqs: [
      0,   2,   4,   6,   8,  10,  12,  14,  16,  18,  20,  22,
     24,  26,  28,  30,  32,  34,  36,  38,  40,  42,  44,  46,
     48,  50,  52,  54,  56,  58,  60,  62,  64,  66,  68,  70,
     72,  74,  76,  78,  80,  82,  84,  86,  88,  90,  92,  94,
     96,  98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118,
    120, 122, 124, 126
  ],
  info: {
    notchFrequency: '60Hz',
    samplingRate: 256,
    startTime: 1628197298732
  },
  psd: [
    [
       98.63572869924877,  278.0499119981597,  396.9075453246308,
      330.93307599602673,  154.4437300666471,   127.381718447909,
      156.28589064508202,  90.27952532968459,  74.02596881179568,
      102.68745491461037,  77.40464372151173,  65.97947493071318,
       93.61333998578448,  70.03755439407374, 47.965913961348285,
       72.11457749610696,  60.14793608854482,  36.43407809513316,
        52.5321191045999, 45.400500672083176, 24.168757651016627,
        37.1839936941784, 35.105296424441036, 14.991272333196237,
      17.013079679743214, 22.931615422127962,   9.64319909169338,
        6.95610789706202,  10.48806813349181,   8.77101666889275,
        8.08687117576467,   7.88454615426007,   7.00857990702008,
       9.129752553805993,  7.500414008219254, 6.4966183674128635,
       7.833399187762861,  7.283708613586358,  5.616493707372124,
       7.336663052350952,  6.859592851990316,  6.153804860755752,
       6.618696201331677,  6.837180878389385, 5.7838083130648945,
       6.562155335152424,  6.093398492507891,  6.073406841367065,
      5.9593899491763205,   6.14611107916922,  5.674535238756583,
      6.0774035077156645,  5.656938723201682,  5.892346415487732,
        5.61605742554047,  5.842031463718972,  5.514410378848478,
       5.803658958523979,   5.47172273287992,  5.745739449800702,
       5.452574435173335,  5.724439426371041, 5.4273919360609035,
       5.707772456903569
    ],
    [
       705.0449351206108, 1355.4773207863375, 1795.4768676020658,
      1480.8269991044856,  879.7073135412625,  734.4677613113015,
       691.6145778964477,  482.9726329188916,  463.9458627254311,
       448.9185196251005,  325.3989179173811,  356.7357077059943,
      366.94089924861487, 288.75232488327777,  304.2605284381872,
       301.8930577524112,  237.4042509842181,   248.189270828571,
      244.01379638689255,  177.6237336667693, 172.43627544841166,
      176.69895192953885, 125.52722189861495, 105.15448954029884,
      106.56146701054848, 63.477588704077554, 33.251603187541896,
       42.84498288204394, 23.928294234593277,  9.767390485089537,
       15.03794181419898, 13.965161093202841, 20.844294981525614,
      12.007423569211078, 11.126393885153014, 20.104729878667776,
      12.319226156469027, 10.486815016962693, 17.143209506256614,
      11.132954923524995,  10.62728760663002, 14.463591856614492,
      10.925935011739528, 10.576245202399233, 12.869498809209984,
      10.551373735436435,  10.90154409382562, 11.496161902596342,
       10.59771747532043, 10.626533456022605, 10.982565808529692,
      10.292226858572462, 10.587506870484761, 10.420838952336604,
       10.33846013622055, 10.228524593265222, 10.333151489515492,
      10.081149399888313,  10.23400481786508, 10.046416371678554,
       10.14064797386651,  9.979626942208188, 10.115418833026341,
       9.962197147976129
    ],
    [
       929.0377610383296, 1793.6811181430987, 2377.6119679334947,
      1958.9102655269323, 1162.3055283149445,  979.7382233236812,
        921.065883147485,  640.2289218688652,  619.3532710184182,
       597.9752360209405, 433.84218492741303, 480.63827859906377,
       494.8759497888118,  388.5592867189369, 408.72806358233913,
       403.8696475504568,  318.0820897599802,  335.6971387951459,
       330.1749076377176,  240.2816149573954,  234.1828700249589,
       238.8172342465352, 168.40453177012395, 141.41297208524767,
       143.3763643586936,  84.85781325822384, 44.693260335642535,
       57.99822015732011,  32.12541610045182, 13.475265334606835,
      20.599681672533375,  19.01837044906831, 28.246044041267428,
      16.189180127175323,  15.41587209212851,  27.05517471975363,
      16.903913745426895,  14.33546383874818, 23.026090510272617,
       14.87036823280212,   14.6068129622348, 19.471383549994453,
       14.96633838574153, 14.387933483886725, 17.466586501671532,
      14.355984995364704, 14.919336874633427, 15.536030663642576,
      14.543171342633388, 14.399423945911408,  15.00275665739408,
      13.982397994287624, 14.474361692225106, 14.126311107434065,
      14.160828645624179,  13.86227555141294, 14.139642435285486,
      13.674442534649062, 14.000882290360456, 13.623523705584073,
      13.881719450096554, 13.533315732597867,  13.84382520692153,
      13.508775392377734
    ],
    [
       461.1411944745596,   865.879891899699, 1150.3297939965412,
       967.6717977233337,  599.5067484775997,  487.7449557189379,
       449.7148527252277, 324.75340665195546,  307.3960653823736,
      289.99356448521917,  218.9307327550319,   241.757776766985,
      249.28709256762335, 206.95217758165205,  213.8552238566172,
      208.04287443336904, 172.16085191285578,  177.8042520513104,
      170.76433578042244,  131.2290615556113, 127.75140879293434,
       125.8563352501824,  94.44550500099892,  81.32600662751962,
       76.33377477822643,  47.53219019300205, 29.403234515228505,
      29.734512582314988,  14.48430634759893,  4.338569856695335,
       7.956256668786119,  7.925904164095972, 12.763456529014546,
       5.823156703304557,  7.213304914646235,  12.53665043042392,
       6.064277734596193, 6.0142267398677225, 10.591216540020291,
       5.491335175417487,  5.995538415704912,   8.41366666249266,
       5.354337464315892,  5.684078918046329,  7.289586947844527,
       5.258040775750918,  5.927892633808341,  6.209024439918837,
      5.5308778688068525,  5.658218846438647,  5.937393602233365,
       5.337787715362042,  5.723456582324143,  5.491309810378187,
       5.517788579034077, 5.3995359451843115,  5.544753793342432,
       5.291402564159946,  5.499716204904763,  5.281561955171903,
      5.4342620388212115,  5.243854533655554,  5.426831995465968,
        5.23668469315059
    ],
    [
      485.28953220351815,  913.8215446531855, 1212.6893063853145,
      1017.6653954348992,  629.0590135927589,  513.8401411331691,
      473.94607162953474,  340.7794194629709,  323.4068209463424,
       304.6140613386581,  227.9530765749002, 253.44275369319936,
      261.96382482250846, 215.95821471824453,  223.2060790303756,
       217.5887331092368, 180.05264499052626,  186.6722683242584,
      178.86415942933493, 135.75616983861607,  132.7145908145038,
       131.7205674261096,  98.13621951582651,  84.22587059556682,
       79.69348482329639,  49.27415323250583, 29.885948066276374,
      31.018207012950032, 15.464201551787149,  4.696597650070098,
       8.680077668220271,  8.409519490488169, 13.587393841532371,
       6.264695355862866,  7.572139679407593,  13.17605643990251,
       6.652754348269858, 6.3465028991975325, 11.306345734652368,
       5.926439990819285,  6.470051702062516,  8.904949649675096,
        5.90150761172456,  6.060485555618185,  7.854198979433359,
       5.663406547398727, 6.4306283909466435,  6.623721018560318,
       6.041438452881903, 6.0442294631002795,  6.444444318919457,
       5.721040377425073,  6.213246144964029, 5.8753004744243755,
       6.002696003640614,  5.774903831465746,  6.026353504659674,
       5.663944879598529,  5.975725903093066,  5.652394044025673,
       5.907643067149823,  5.612177778683849,  5.898257253854689,
       5.604260960707902
    ],
    [
       703.9620591951088, 1348.1617601998341,  1787.817378338989,
      1480.9682977349662,  887.8732586924484,  741.7489045127593,
       696.4862482257432, 486.69267953812624, 464.30488178918847,
      448.10745320129496,  329.6131727268781,  364.1234842222161,
      375.17667115955084, 296.30580382389024,  307.6916385785675,
       303.4585158601969,  241.4840430193035,  253.3373457325428,
      248.14875370587004,  181.8456760420915, 176.16078095306457,
      178.58969714768043,  126.8938114163353,  106.7131960446341,
      106.86715498126117, 63.565099293832944,  33.94124074989405,
       42.78261882478681, 23.418093057211088,  9.598376452708248,
        14.8564635663729,  13.73158527388318, 20.632309203759725,
      11.571312623082235,  11.16199944105178,  19.71697966916169,
      12.151289348370563,  10.27332116826051,  16.93453042721219,
      10.734196078665759, 10.578983816474802,  14.17031151713728,
      10.741999390916682, 10.370828224990875, 12.669038407738478,
      10.290437631963869, 10.794986602960588, 11.204752776686476,
      10.481500894235385, 10.373479646590457, 10.845762801813153,
       10.04623630410688, 10.466118545780976,  10.16324823810254,
      10.225788013632457,  9.975974411529377,  10.21577779934349,
       9.834755780463283, 10.117741157508208,  9.799067226573825,
      10.029038431063377,  9.733625015451048, 10.002552468346979,
        9.71630020598175
    ],
    [
       753.3573854351718, 1451.3463711535637, 1925.4394750722938,
      1592.2479396735228,  950.1320711729846,  793.4163539564408,
        744.990261771651,  519.4611344925438,  498.6282329256233,
       480.4651411728872,  349.9224396629356, 388.08464608248545,
      400.41433150212987, 314.28699618071386,  328.3871848882801,
      325.21671199729667, 257.08898576447365,  270.0756790958063,
      265.56055695000117, 193.58422699465976,  187.3975181698473,
       190.5723885919431,  134.7850068920377, 113.55417235960783,
      114.65352872167782,  67.97249319078067,  36.07066166066659,
      46.193455592634194, 25.446519462818365, 10.645647869461468,
       16.33292205396577, 15.082694752225358, 22.479081487850554,
      12.660457753439347, 12.331655605615103, 21.469122245638992,
      13.259611882976637, 11.366093905761021,   18.4614508154199,
      11.778790555694387, 11.710458297806564, 15.485077358432786,
      11.805213571500564, 11.446226210170733, 13.887884653568616,
      11.334007371207884, 11.881804314077982,  12.30654501069072,
      11.528873716721828, 11.419099102496702, 11.910897138255397,
      11.059631088502826, 11.505557872713792, 11.178885987141047,
      11.242816922347224,  10.97697117415906, 11.227884136208706,
      10.822693801769324, 11.121177549665633, 10.782078947654583,
      11.024368739435461, 10.711151846144949, 10.995151378799578,
      10.691866595209362
    ],
    [
       367.4136193009799,  826.7329948628463, 1118.3539023221265,
        890.162220791093,  436.1682590608995,  391.4382314784865,
      417.04217210936963, 251.56740893464422,  238.5284921292077,
       267.6000138141995,   168.617128049186, 165.98870799455165,
      200.56943140232212, 129.37112302840023, 126.00839013852573,
      162.39587433692205, 109.20332945126022,  87.00867663058928,
      117.95711115144483,  83.29961985396704,  58.57022651921219,
       86.68284556964056,  63.23057486573713, 22.615043247176825,
       45.79353231282386,  39.94573246684187,  6.411920387449734,
      21.964845928081306, 21.959370088243116, 16.277025835788837,
      16.547064843486048, 15.715335138181468, 16.607457789253704,
      17.537478155658583, 13.336615276197591, 15.835823046176726,
      15.461292461652397, 13.730332854951738,  13.27865408978899,
      14.709605078820157,   12.9045807988706, 13.692853045756497,
      13.258453124525246, 13.287331440282053, 12.481768554519784,
      13.223425784019863, 12.187280042833416, 12.738723198131671,
      12.048047848217715,  12.49122466572343, 11.744286244430379,
      12.342663893673903, 11.552471648965968, 12.117055516659004,
      11.432033986591367, 11.965037193629023, 11.288502743059457,
      11.863912386218576, 11.190384199321217, 11.771734261131785,
      11.131137815008097,  11.71660417394918,  11.08761147894627,
      11.686948260719255
    ]
  ]
}
```

Please note this data is pre-filtered using the same filters describe under the `raw` data parameter: notch and band pass.

### Power By Band

```python
def callback(data):
    print("data", data)

unsubscribe = neurosity.brainwaves_power_by_band(callback)
```

The code above will output new epochs 4 times a second. Every frequency label (e.g. beta) contains an average power value per channel.

Here's an example of 1 event:

```
{
  label: 'powerByBand',
  data: {
    alpha: [
      0.4326838933650053,
      0.7011913998347046,
      1.3717684682104212,
      0.4043711439234614,
      0.4276277910286375,
      0.7343967679911133,
      0.4643529443786634,
      0.5012185195340365
    ],
    beta: [
      1.0473270376446968,
      0.6565360935142369,
      0.9905849734272257,
      0.4167252084581245,
      0.5812834985846604,
      0.9092642713573444,
      0.9963075404421067,
      1.0495665446734443
    ],
    delta: [
      0.46131690566460004,
      1.0030278320362798,
      0.8563781797682917,
      0.2911634678359473,
      0.5829804845703581,
      0.6714666592936025,
      0.37730719195446316,
      1.0851178080710937
    ],
    gamma: [
      0.22648773160183822,
      0.2171827127990081,
      0.2626969784220435,
      0.16349594919353772,
      0.17327387900192714,
      0.18990085940799623,
      0.22908540295491436,
      0.2537584109981627
    ],
    theta: [
      0.6434504807739541,
      0.936240328507981,
      0.8679595766147628,
      0.23662065697316603,
      0.6048174207817718,
      0.816112075629094,
      0.3367745804938397,
      1.1043745310136739
    ]
  }
}
```

Please note this data is pre-filtered using the same filters describe under the `brainwaves_raw` method: notch and band pass.

### Adding Markers

```python
def callback(data):
    print("data", data)

unsubscribe = neurosity.brainwaves_raw(callback)
time.sleep(2)
neurosity.add_marker("eyes-closed")
time.sleep(2)
unsubscribe()
```

## Signal Quality

Standard deviation based signal quality metrics. Great signal happens when the standard deviation is between 1.5 and 10.

```python
def callback(data):
    print("data", data)

unsubscribe = neurosity.signal_quality(callback)
```

## Accelerometer

```python
def callback(data):
    print("data", data)

unsubscribe = neurosity.accelerometer(callback)
```

## Calm

Constantly fires and predicts user's calm level from passive cognitive state. Calm is a probability from 0.0 to 1.0. To get calm over 0.3 is significant. Calm will take up to 16 seconds to initialize. We normally take a longer rolling average of calm to produce brain processes over time, see how we do it in our flow walk through.

Things that can help increase the calm score are:

- Closing your eyes for 30 seconds or more
- Seating or standing still
- Breathing exercises
- Meditating

```python
def callback(data):
    print("data", data)

    # { probability: 0.34, metric: "awareness", label: "calm", timestamp:  1569961321101 }
    # { probability: 0.41, metric: "awareness", label: "calm", timestamp:  1569961321105 }
    # { probability: 0.45, metric: "awareness", label: "calm", timestamp:  1569961321110 }

unsubscribe = neurosity.calm(callback)
```

## Focus

Constantly fires and predicts user's focus level from passive cognitive state based on the gamma brainwave between 30 and 44 Hz. Focus is a probability from 0.0 to 1.0. To get focus over 0.3 is significant. Focus will take up to 16 seconds to fully initialize.

```python
def callback(data):
    print("data", data)

    # { probability: 0.51, metric: "awareness", label: "focus", timestamp:  1569961321102 }
    # { probability: 0.56, metric: "awareness", label: "focus", timestamp:  1569961321106 }
    # { probability: 0.62, metric: "awareness", label: "focus", timestamp:  1569961321111 }

unsubscribe = neurosity.focus(callback)
```

## Kinesis

The Kinesis API is based on the Motor Imagery BCI method. Fires when a user attempts to trigger a side effect from defined thoughts. E.g. motor imagery, etc.

Kinesis implements a spike detection algorithm over the predictions stream.

To train a Kinesis command, use [console.neurosity.co](https://console.neurosity.co) and use the corresponding label for the Active classifier. Learn how to train a new command [here](https://support.neurosity.co/hc/en-us/articles/360036344012-Imagined-thought-training).

```python
def callback(data):
    print("data", data)
    # Switch light off/on
    light.togglePower()

    # { probability: 0.93, label: "rightArm", timestamp: 1569961321174, metric: "kinesis" }


unsubscribe = neurosity.kinesis("rightArm", callback)
```

Or:

```python
def callback(data):
    print("data", data)
    # Launch drone
    drone.launch()

    # { probability: 0.92, label: "leftArm", timestamp: 1569961321191, type: "kinesis"  }

unsubscribe = neurosity.kinesis("leftArm", callback)
```

## Device Info

```python
info = neurosity.get_info()
print(info)

# { apiVersion: string,  channelNames: string[], channels: number,
#  deviceId: string, deviceNickname: string, manufacturer: string, model: string,
#  modelName: string, modelVersion: string, osVersion: string, samplingRate: number }
```

## Device Status

### Metrics:

- state: "online" | "offline" | "shuttingOff" | "updating" | "booting"
- sleepMode: boolean
- sleepModeReason: "updating" | "charging" | null
- charging: boolean
- battery: number
- lastHeartbeat: number
- ssid: string
- claimedBy: string

### Get Status Once

```python
status = neurosity.status_once()
print(status)

# { state: "online", charging: true, battery: 93, ... }
```

### Stream Status

```python
def callback(data):
    print("data", data)
    # { state: "online", charging: true, battery: 93, ... }


unsubscribe = neurosity.status(callback)
```

## Device Settings

```python
def callback(data):
    print("data", data)
    # { lsl: false, osc: false }

unsubscribe = neurosity.settings(callback)
```

## Develop

### Setting up the environment

Use the Dev Container extension within VSCode for a stable and consistent development experience.

Install all the requirements for development:

```bash
pip install -r requirements.txt -r dev-requirements.txt
pip install -e .
```

### Running the Example

Run from the root directory after setting up your development environment above:

```bash
python examples/example.py
```

## Code of Conduct

This project has adopted a [Code of Conduct](CODE_OF_CONDUCT.md). Contact [opensource@neurosity.co](mailto:opensource@neurosity.co) with any additional questions or comments.

## License

Copyright (c) Neurosity, Inc. All rights reserved.

Licensed under the [MIT license](LICENSE).
