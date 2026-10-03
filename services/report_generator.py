import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_pdf_report(df, stats):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    elements = []
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'ReportTitle',
        parent=styles['Heading1'],
        fontSize=22,
        textColor=colors.HexColor('#0f172a'),
        spaceAfter=6
    )
    subtitle_style = ParagraphStyle(
        'ReportSubtitle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#64748b'),
        spaceAfter=20
    )
    heading_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#1e293b'),
        spaceBefore=15,
        spaceAfter=10
    )
    
    # Title & Metadata
    elements.append(Paragraph("Ocean Climate Intelligence Report", title_style))
    elements.append(Paragraph("Generated automatically by OceanClimate Platform v2.0", subtitle_style))
    elements.append(Spacer(1, 10))
    
    # Summary Statistics Table
    elements.append(Paragraph("Executive Summary Statistics", heading_style))
    summary_data = [
        ['Metric', 'Value'],
        ['Average Surface Temperature', f"{stats.get('avg', 0)} °C"],
        ['Minimum Temperature', f"{stats.get('min', 0)} °C"],
        ['Maximum Temperature', f"{stats.get('max', 0)} °C"],
        ['Temperature Anomaly', f"{stats.get('anomaly', 0)} °C"]
    ]
    
    t_summary = Table(summary_data, colWidths=[250, 250])
    t_summary.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0f172a')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f8fafc')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8fafc')])
    ]))
    elements.append(t_summary)
    elements.append(Spacer(1, 20))
    
    # Recent Observations Table Snippet
    elements.append(Paragraph("Recent Telemetry Observations", heading_style))
    if not df.empty:
        obs_data = [['Date', 'Temp (°C)', 'Wave Height (m)', 'Wind Speed (km/h)']]
        for _, row in df.tail(10).iterrows(): # Show last 10 records
            obs_data.append([str(row['Date']), str(row['Temp_C']), str(row['Wave_Height_m']), str(row['Wind_Speed_kmh'])])
            
        t_obs = Table(obs_data, colWidths=[125, 125, 125, 125])
        t_obs.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3b82f6')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
        ]))
        elements.append(t_obs)
    
    doc.build(elements)
    buffer.seek(0)
    return buffer.getvalue()