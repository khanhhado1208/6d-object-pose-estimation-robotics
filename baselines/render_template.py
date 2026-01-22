import os
import open3d as o3d

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
mesh_path = os.path.join(BASE_DIR, 'data', 'lm', 'models', 'obj_000001.ply')
saved_path = os.path.join(BASE_DIR, 'assets', 'template_000.png')

# Load mesh
mesh = o3d.io.read_triangle_mesh(mesh_path)
mesh.compute_vertex_normals()
print(mesh)

# Create visualizer
vis = o3d.visualization.Visualizer()
vis.create_window(visible=True)
vis.add_geometry(mesh)

# Set up camera
ctr = vis.get_view_control()

# Set view 
ctr.set_front([0.0, 0.0, -1.0]) # Camera looks along negative z-axis
ctr.set_lookat(mesh.get_center()) # Look at the center of the mesh
ctr.set_up((0.0, -1.0, 0.0)) # Set the up direction
ctr.set_zoom(0.7) # Zoom level

# Render 1 frame
vis.poll_events()
vis.update_renderer()

# Capture image
vis.capture_screen_image(saved_path)
print(f"Saved rendered image to {saved_path}")
vis.destroy_window() 
