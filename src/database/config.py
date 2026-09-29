from supabase import create_client, Client

SUPABASE_URL = "https://iqtpnptetdecmskjcryo.supabase.co"

SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlxdHBucHRldGRlY21za2pjcnlvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODk3MDg1MzgsImV4cCI6MjEwNTI4NDUzOH0.w6oFLhvtyhSSXSXDaHhCL2LdOJXZUjWxYQ8CO9_X_X4"

print("CONFIG LOADED:", __file__)
print("KEY START:", SUPABASE_KEY[:30])
print("KEY LENGTH:", len(SUPABASE_KEY))

supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)