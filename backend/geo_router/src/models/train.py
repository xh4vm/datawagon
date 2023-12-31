import uuid
import enum
from pydantic import Field
from typing import Any

from .base import JSONModel
from .datetime import RangeDateTime
from .geo import GeoPointOperdate, GeoJSONType


class WagonType(enum.Enum):
    DANGER = "danger"


class WagonStatus(enum.Enum):
    LOADED = "loaded"


class WagonData(JSONModel):
    number: int = Field(description="Номер вагона", examples=[10])
    disls: list[GeoPointOperdate] = Field(
        description="Точки пути",
        examples=[
            [
                {
                    "title": "Звенигород",
                    "geo": {"coordinates": [37.5362099, 55.7668608], "type": "Point"},
                    "operdate": "2023-08-30 01:02:00",
                },
                {
                    "title": "Дмитров",
                    "geo": {"coordinates": [37.5347034, 55.7611376], "type": "Point"},
                    "operdate": "2023-08-30 01:02:00",
                },
            ]
        ],
    )


class TrainData(JSONModel):
    train_index: str
    wagon_counts: int = Field(description="Количество вагонов", examples=[1])
    wagons: list[WagonData]
    railway: GeoJSONType = Field(
        description="Полный маршрут",
        examples=[
            {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [37.5362099, 55.7668608],
                        [37.536251, 55.7671476],
                        [37.5362921, 55.7674066],
                        [37.5363579, 55.7676733],
                        [37.5364319, 55.7679137],
                        [37.5365223, 55.7681727],
                        [37.5366594, 55.7684656],
                        [37.5368676, 55.7688171],
                        [37.537106, 55.7691439],
                        [37.5373746, 55.7694738],
                        [37.5375774, 55.769694200000004],
                        [37.5378048, 55.7699285],
                        [37.5380569, 55.7701643],
                        [37.5382652, 55.7703493],
                        [37.5386461, 55.7706453],
                        [37.5390297, 55.770915],
                        [37.5394051, 55.7711509],
                        [37.5397833, 55.7713636],
                        [37.5401423, 55.7715486],
                        [37.5404173, 55.7716763],
                        [37.540504, 55.7717166],
                        [37.5409178, 55.7718907],
                        [37.5413672, 55.7720665],
                        [37.541707, 55.7721774],
                        [37.5420249, 55.7722869],
                        [37.5423619, 55.7723809],
                        [37.5427483, 55.7724811],
                        [37.5431649, 55.7725828],
                        [37.543776, 55.7727046],
                        [37.5445378, 55.7728248],
                        [37.545031, 55.7728865],
                        [37.5458065, 55.7729512],
                        [37.5464212, 55.7730001],
                        [37.5478609, 55.773088],
                    ],
                    [
                        [37.5883748, 55.7917392],
                        [37.5883122, 55.7915949],
                        [37.5881908, 55.7911772],
                        [37.5880512, 55.7907516],
                        [37.5879165, 55.7902378],
                        [37.5878129, 55.7897028],
                    ],
                    [[37.5360883, 55.7659954], [37.5362099, 55.7668608]],
                    [
                        [37.5878129, 55.7897028],
                        [37.5877667, 55.7894538],
                        [37.587719, 55.7891765],
                        [37.587644, 55.7887152],
                        [37.5875541, 55.7881912],
                        [37.5874028, 55.7875836],
                        [37.5872529, 55.7870764],
                        [37.5871153, 55.786586],
                        [37.5870055, 55.7860541],
                        [37.5868984, 55.7855974],
                        [37.5867262, 55.7849515],
                        [37.586565, 55.784441],
                        [37.5862786, 55.7835034],
                        [37.5862476, 55.7834032],
                        [37.58622, 55.7833141],
                        [37.5861302, 55.7829807],
                        [37.5858486, 55.7819641],
                        [37.5856635, 55.7814724],
                        [37.5854301, 55.7809204],
                        [37.585237, 55.7805448],
                        [37.5850895, 55.7803049],
                        [37.5849178, 55.7800591],
                        [37.5846764, 55.7797981],
                        [37.5843975, 55.7795176],
                        [37.5840139, 55.7792038],
                        [37.5836518, 55.7789383],
                        [37.5832774, 55.7786789],
                        [37.5827377, 55.7783338],
                        [37.5823094, 55.7780575],
                    ],
                    [
                        [37.5243488, 55.7475409],
                        [37.5247666, 55.7476815],
                        [37.5252199, 55.7478324],
                        [37.5256303, 55.7480121],
                        [37.5263947, 55.7483684],
                        [37.5272477, 55.748782],
                        [37.5278699, 55.7491156],
                        [37.5285163, 55.7495277],
                        [37.5288474, 55.7497699],
                        [37.5294978, 55.7503234],
                        [37.5297877, 55.7506116],
                        [37.5300313, 55.750898],
                        [37.5302866, 55.7512018],
                        [37.5304985, 55.7515294],
                        [37.5308526, 55.7521905],
                        [37.5323424, 55.7556204],
                    ],
                    [
                        [37.4481958, 55.7267592],
                        [37.44908, 55.7267804],
                        [37.4498689, 55.7268303],
                        [37.450403, 55.7268789],
                        [37.4510932, 55.7269591],
                        [37.452351, 55.7271405],
                        [37.4537417, 55.7273721],
                        [37.454872, 55.7275509],
                        [37.4608598, 55.7285033],
                        [37.4678211, 55.7295932],
                        [37.4702952, 55.7299307],
                        [37.470597, 55.7299766],
                    ],
                    [[37.5323424, 55.7556204], [37.5325638, 55.7560912]],
                    [
                        [37.5347034, 55.7611376],
                        [37.534825, 55.7613948],
                        [37.534922, 55.7616345],
                        [37.5350864, 55.7620323],
                        [37.5352508, 55.762464],
                        [37.5353687, 55.7628139],
                        [37.5355029, 55.7632256],
                        [37.5355961, 55.763537],
                        [37.535703, 55.7638824],
                        [37.5357989, 55.7641938],
                        [37.5358592, 55.7644266],
                        [37.5359167, 55.7647719],
                        [37.5359743, 55.7651327],
                        [37.5360236, 55.7655088],
                        [37.5360811, 55.765902],
                        [37.5360883, 55.7659954],
                    ],
                    [
                        [37.3839264, 55.7189382],
                        [37.3876321, 55.7202842],
                        [37.391873, 55.721782],
                        [37.3934637, 55.7223327],
                        [37.3951637, 55.7229456],
                        [37.3967335, 55.7235031],
                    ],
                    [
                        [37.3201166, 55.6839905],
                        [37.321004, 55.6843599],
                        [37.3225992, 55.6851153],
                        [37.3253364, 55.6865123],
                        [37.3265068, 55.6871715],
                        [37.326906, 55.6873743],
                        [37.327328, 55.6875975],
                        [37.328123, 55.688054],
                        [37.3289032, 55.6885243],
                        [37.3292609, 55.6887772],
                        [37.3296917, 55.6891123],
                        [37.3303096, 55.6896313],
                        [37.330946, 55.6902274],
                    ],
                    [[37.5552877, 55.7738215], [37.5544149, 55.773729]],
                    [
                        [37.5564228, 55.7739292],
                        [37.5569572, 55.7739712],
                        [37.5589058, 55.7741586],
                        [37.5594342, 55.7742102],
                        [37.5600404, 55.7742698],
                        [37.5616422, 55.7744424],
                        [37.5623727, 55.7745211],
                        [37.5638598, 55.7746658],
                        [37.565299, 55.77482],
                        [37.5659802, 55.7748926],
                        [37.5671935, 55.7750218],
                        [37.568406, 55.7751462],
                        [37.5690573, 55.7752134],
                        [37.5695437, 55.7752649],
                        [37.5703167, 55.7753388],
                        [37.5708499, 55.7753963],
                        [37.5710937, 55.775416],
                        [37.5717227, 55.7754507],
                        [37.5720339, 55.7754605],
                        [37.572562, 55.775474],
                        [37.57321, 55.7754597],
                        [37.5734031, 55.775459],
                        [37.5738235, 55.7754503],
                    ],
                    [[37.5564228, 55.7739292], [37.5552877, 55.7738215]],
                    [
                        [37.4896882, 55.7329684],
                        [37.4955136, 55.7339159],
                        [37.496995, 55.7341995],
                        [37.4985586, 55.7345644],
                        [37.4994103, 55.7347988],
                        [37.5036389, 55.7360569],
                        [37.5052671, 55.736565],
                        [37.5059282, 55.7367931],
                        [37.5066269, 55.7370913],
                        [37.5073376, 55.7374614],
                        [37.5081301, 55.7379596],
                        [37.5089027, 55.7385108],
                        [37.5094727, 55.7390083],
                        [37.5101494, 55.739754],
                        [37.5103866, 55.7400037],
                        [37.5117405, 55.7414287],
                        [37.5134413, 55.7430078],
                        [37.5137937, 55.7433365],
                        [37.5140754, 55.743575],
                        [37.5143678, 55.7437969],
                        [37.5146821, 55.7440282],
                        [37.5147755, 55.7440928],
                        [37.5152126, 55.7443707],
                        [37.5160066, 55.7448145],
                        [37.516657, 55.7451475],
                        [37.5171465, 55.7453913],
                        [37.5176132, 55.7455981],
                        [37.5180745, 55.7457717],
                        [37.5185895, 55.7459257],
                        [37.5192788, 55.7461039],
                        [37.5202873, 55.7463635],
                        [37.5212645, 55.7466308],
                    ],
                    [
                        [37.3572655, 55.7094626],
                        [37.3600054, 55.7104401],
                        [37.3638578, 55.7118093],
                        [37.3652463, 55.7122997],
                        [37.3670307, 55.7129314],
                        [37.3687306, 55.7135425],
                        [37.3709087, 55.7143043],
                        [37.3731041, 55.7150877],
                        [37.3746094, 55.7156335],
                        [37.375323, 55.7158871],
                        [37.377114, 55.7165228],
                        [37.3826561, 55.7184907],
                    ],
                    [
                        [37.3424346, 55.6998778],
                        [37.342676, 55.7000503],
                        [37.3427446, 55.7000993],
                    ],
                    [
                        [37.4752103, 55.7307054],
                        [37.4759271, 55.7308163],
                        [37.4781859, 55.7312169],
                        [37.4889685, 55.732848],
                    ],
                    [
                        [37.470597, 55.7299766],
                        [37.4723265, 55.7302498],
                        [37.4752103, 55.7307054],
                    ],
                    [
                        [37.5478609, 55.773088],
                        [37.5494498, 55.7731693],
                        [37.5500558, 55.7732164],
                        [37.5504944, 55.7732564],
                        [37.5519267, 55.7734336],
                        [37.5525907, 55.7735097],
                        [37.5534163, 55.7736131],
                        [37.5544149, 55.773729],
                    ],
                    [
                        [37.4024697, 55.72554],
                        [37.4033659, 55.7258219],
                        [37.404287, 55.7260596],
                        [37.4054972, 55.7263447],
                        [37.4063134, 55.7264866],
                        [37.4069795, 55.7265906],
                        [37.4076229, 55.726676],
                        [37.4083481, 55.7267556],
                        [37.4085382, 55.7267714],
                        [37.4091296, 55.7268099],
                        [37.4098386, 55.7268398],
                        [37.4104872, 55.7268528],
                        [37.4112568, 55.7268556],
                        [37.4121581, 55.7268537],
                    ],
                    [
                        [37.330946, 55.6902274],
                        [37.33232, 55.6915856],
                        [37.3339777, 55.6932562],
                        [37.3350819, 55.6943004],
                        [37.3358292, 55.6949447],
                        [37.3365966, 55.6955777],
                        [37.3373995, 55.6962484],
                        [37.3384784, 55.6970284],
                        [37.3401061, 55.6981897],
                        [37.3414837, 55.6991983],
                        [37.3424346, 55.6998778],
                    ],
                    [
                        [37.3427446, 55.7000993],
                        [37.3444437, 55.7013134],
                        [37.3470162, 55.7031247],
                        [37.3495563, 55.7049349],
                        [37.35138, 55.7062352],
                        [37.3519142, 55.7066147],
                        [37.3524833, 55.7070189],
                        [37.3530653, 55.7074136],
                    ],
                    [
                        [37.3530653, 55.7074136],
                        [37.3535022, 55.7077041],
                        [37.3540504, 55.7080359],
                        [37.3545264, 55.7082881],
                        [37.3551522, 55.7086016],
                        [37.35556, 55.7087945],
                        [37.3561591, 55.7090374],
                        [37.356596, 55.7092055],
                        [37.3572655, 55.7094626],
                    ],
                    [
                        [37.4121581, 55.7268537],
                        [37.413729, 55.7268402],
                        [37.4201198, 55.7268062],
                    ],
                    [
                        [37.3968114, 55.7235307],
                        [37.3968456, 55.7235429],
                        [37.4024697, 55.72554],
                    ],
                ],
            }
        ],
    )
