import pandas as pd

# Tạo dữ liệu cho từng bảng
ngon_ngu = pd.DataFrame({
    "Ngôn ngữ": ["Python", "HTML/CSS", "JavaScript", "PHP", "TypeScript", "Kotlin"],
    "Số dự án": ["~25", "~15", "~8", "6", "4", "3"],
    "Mức độ thành thạo": ["Xuất sắc ⭐⭐⭐⭐⭐", "Tốt ⭐⭐⭐⭐", "Khá ⭐⭐⭐", "Khá ⭐⭐⭐", "Trung bình ⭐⭐", "Cơ bản ⭐⭐"]
})

linh_vuc = pd.DataFrame({
    "Lĩnh vực": ["AI & Machine Learning", "Web Development", "Data Analysis", "Bảo mật & Mã hóa", "Mobile Development", "Game Development"],
    "Mức độ thành thạo": ["Xuất sắc ⭐⭐⭐⭐⭐", "Tốt ⭐⭐⭐⭐", "Tốt ⭐⭐⭐⭐", "Tốt ⭐⭐⭐⭐", "Khá ⭐⭐⭐", "Khá ⭐⭐⭐"],
    "Dự án tiêu biểu": [
        "AI-machine-and-deep-learning; AIFaceDetectionProject; Vertex-AI-Reasoning-Agent-Demo",
        "FULL-STACK-AI-APP; PHP-master-page; unicornbrand",
        "Sales-Data-Analysis; Python-data-analyze-visual; Candlestick-Chart-Plot",
        "Information-Security; SecureGamer; RSA-3",
        "Spiketune-android-mobile-app; Mobile-device-programming",
        "Pro-snake-game; Project-Report-Ultimate-Caro"
    ]
})

cong_nghe = pd.DataFrame({
    "Công nghệ/Framework": ["Firebase", "Flask", "SQL Server", "Next.js", "Pygame"],
    "Mức độ sử dụng": ["Thường xuyên", "Thường xuyên", "Thường xuyên", "Đã từng sử dụng", "Đã từng sử dụng"]
})

diem_manh = pd.DataFrame({
    "Điểm mạnh nổi bật": [
        "Đa dạng tech stack, khả năng học hỏi nhanh",
        "Mạnh về AI/ML và xử lý dữ liệu",
        "Kinh nghiệm phát triển web full-stack",
        "Kiến thức về bảo mật và mã hóa",
        "Có thể phát triển ứng dụng đa nền tảng"
    ]
})

huong_pt = pd.DataFrame({
    "Hướng phát triển đề xuất": [
        "Đào sâu thêm về Cloud Computing",
        "Tăng cường kiến thức DevOps",
        "Phát triển kỹ năng Mobile Development",
        "Nghiên cứu thêm về Blockchain"
    ]
})

# Xuất ra file Excel
with pd.ExcelWriter("/mnt/data/Bang_Danh_Gia_Ky_Nang_Lap_Trinh.xlsx", engine="openpyxl") as writer:
    ngon_ngu.to_excel(writer, sheet_name="Ngôn ngữ", index=False)
    linh_vuc.to_excel(writer, sheet_name="Lĩnh vực", index=False)
    cong_nghe.to_excel(writer, sheet_name="Công nghệ", index=False)
    diem_manh.to_excel(writer, sheet_name="Điểm mạnh", index=False)
    huong_pt.to_excel(writer, sheet_name="Hướng phát triển", index=False)
