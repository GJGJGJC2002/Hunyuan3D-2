import sys
sys.path.insert(0, '/home/gejunchen/Work/2025-6/Baseline/Hunyuan3D-2.1/hy3dshape')
sys.path.insert(0, '/home/gejunchen/Work/2025-6/Baseline/Hunyuan3D-2.1/hy3dpaint')

from PIL import Image
from hy3dshape.rembg import BackgroundRemover
from hy3dshape.pipelines import Hunyuan3DDiTFlowMatchingPipeline


# from textureGenPipeline import Hunyuan3DPaintPipeline, Hunyuan3DPaintConfig


def get_rembg_image(img):
    image = Image.open(img).convert("RGBA")
    if image.mode == 'RGB':
        rembg = BackgroundRemover()
        image = rembg(image)
    return image

def genete_shape(img):
    model_path = 'tencent/Hunyuan3D-2.1'
    pipeline_shapegen = Hunyuan3DDiTFlowMatchingPipeline.from_pretrained(model_path)

    image = Image.open(img).convert("RGBA")
    if image.mode == 'RGB':
        rembg = BackgroundRemover()
        image = rembg(image)

    mesh = pipeline_shapegen(image=image)[0]
    
    return mesh, image


if __name__ == "__main__":
    try:
        from torchvision_fix import apply_fix
        apply_fix()
    except ImportError:
        print("Warning: torchvision_fix module not found, proceeding without compatibility fix")                                      
    except Exception as e:
        print(f"Warning: Failed to apply torchvision fix: {e}")

    # shape
    model_path = 'tencent/Hunyuan3D-2.1'
    pipeline_shapegen = Hunyuan3DDiTFlowMatchingPipeline.from_pretrained(model_path)

    image_path = 'assets/demo.png'
    image = Image.open(image_path).convert("RGBA")
    if image.mode == 'RGB':
        rembg = BackgroundRemover()
        image = rembg(image)

    mesh = pipeline_shapegen(image=image)[0]
    mesh.export('demo.glb')

    # # paint
    # max_num_view = 6  # can be 6 to 9
    # resolution = 512  # can be 768 or 512
    # conf = Hunyuan3DPaintConfig(max_num_view, resolution)
    # conf.realesrgan_ckpt_path = "hy3dpaint/ckpt/RealESRGAN_x4plus.pth"
    # conf.multiview_cfg_path = "hy3dpaint/cfgs/hunyuan-paint-pbr.yaml"
    # conf.custom_pipeline = "hy3dpaint/hunyuanpaintpbr"
    # paint_pipeline = Hunyuan3DPaintPipeline(conf)

    # output_mesh_path = 'demo_textured.glb'
    # output_mesh_path = paint_pipeline(
    #     mesh_path = "demo.glb", 
    #     image_path = 'assets/demo.png',
    #     output_mesh_path = output_mesh_path
    # )
