"""
config start wandb at Path.home() / ".config" / sub_dir
ultralytics.__version__ == 8.1.24
Running with multi gpu should add ../KataCR to your PYTHONPATH in .bashrc or .zshrc
export PYTHONPATH=$PYTHONPATH:/Your/Path/KataCR
"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[2]))
from ultralytics.cfg import get_cfg
from ultralytics.engine.model import Model
from pathlib import Path
from katacr.yolov8.custom_model import CRDetectionModel
from katacr.yolov8.custom_validator import CRDetectionValidator
from katacr.yolov8.custom_trainer import CRTrainer
from katacr.yolov8.custom_predict import CRDetectionPredictor

class YOLO_CR(Model):
  """YOLO (You Only Look Once) object detection model. (Clash Royale)"""

  def __init__(self, model="yolov8n.pt", task=None, verbose=False):
    super().__init__(model=model, task=task, verbose=verbose)

  @property
  def task_map(self):
    """Map head to model, trainer, validator, and predictor classes."""
    return {
      "detect": {
        "model": CRDetectionModel,
        "trainer": CRTrainer,
        "validator": CRDetectionValidator,
        "predictor": CRDetectionPredictor,
      },
    }

if __name__ == '__main__':
  model = YOLO_CR("yolov8x.yaml", task='detect')
  model.train(**dict(get_cfg('./katacr/yolov8/ClashRoyale.yaml')))
