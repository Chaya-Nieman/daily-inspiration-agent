"""
template.py

Generates the full HTML email by wrapping the agent's content snippet
in a modern, Gmail-compatible email layout.
"""


def build_email_html(content_snippet: str) -> str:
    """
    Wraps the agent-generated HTML snippet in a styled email template.

    Args:
        content_snippet: The inner HTML produced by the agent
                         (blockquote, author, reflection elements).

    Returns:
        A complete HTML string ready to be sent as an email body.
    """
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Daily Inspiration</title>
</head>
<body style="margin:0; padding:0; background-color:#f0f4f8; font-family: Georgia, 'Times New Roman', serif;">

  <!-- Outer wrapper -->
  <table width="100%" cellpadding="0" cellspacing="0" border="0"
         style="background-color:#f0f4f8; padding: 40px 20px;">
    <tr>
      <td align="center">

        <!-- Card -->
        <table width="600" cellpadding="0" cellspacing="0" border="0"
               style="background-color:#ffffff; border-radius:16px;
                      box-shadow: 0 4px 24px rgba(0,0,0,0.08);
                      overflow:hidden; max-width:600px;">

          <!-- Header -->
          <tr>
            <td align="center"
                style="background: linear-gradient(135deg, #a8c8e8 0%, #d4a8d4 100%);
                       padding: 36px 40px 28px;">
              <h1 style="margin:0; font-size:28px; color:#ffffff;
                         letter-spacing:2px; font-weight:normal;
                         text-shadow: 0 1px 3px rgba(0,0,0,0.15);">
                ✨ Daily Inspiration ✨
              </h1>
            </td>
          </tr>

          <!-- Content body -->
          <tr>
            <td style="padding: 40px 48px 32px;">

              <!-- Quote block -->
              <blockquote style="margin: 0 0 20px 0; padding: 24px 28px;
                                  background-color:#f8f4ff;
                                  border-left: 4px solid #b39ddb;
                                  border-radius: 8px;
                                  font-size: 20px; line-height: 1.7;
                                  color: #3d3560; font-style: italic;">
                {_extract_quote(content_snippet)}
              </blockquote>

              <!-- Author -->
              <p class="author"
                 style="margin: 0 0 28px 0; text-align:right;
                        font-size:15px; color:#7e57c2;
                        font-weight:bold; letter-spacing:0.5px;">
                {_extract_author(content_snippet)}
              </p>

              <!-- Divider -->
              <hr style="border:none; border-top:1px solid #e8e0f0; margin: 0 0 28px 0;" />

              <!-- Reflection -->
              <p class="reflection"
                 style="margin:0; font-size:16px; line-height:1.8;
                        color:#5a5a7a; font-style:normal;">
                {_extract_reflection(content_snippet)}
              </p>

            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td align="center"
                style="background-color:#f8f4ff; padding: 24px 40px;
                       border-top: 1px solid #e8e0f0;">
              <p style="margin:0; font-size:15px; color:#9e86c8; letter-spacing:0.5px;">
                Have a wonderful day 🌷
              </p>
            </td>
          </tr>

        </table>
        <!-- /Card -->

      </td>
    </tr>
  </table>

</body>
</html>"""
    return html


def _extract_quote(snippet: str) -> str:
    """Pull the text inside <blockquote>...</blockquote>, or return the full snippet."""
    import re
    match = re.search(r'<blockquote[^>]*>(.*?)</blockquote>', snippet, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return snippet


def _extract_author(snippet: str) -> str:
    """Pull the author name from a <p class='author'> tag."""
    import re
    match = re.search(r'<p[^>]*class=["\']author["\'][^>]*>(.*?)</p>', snippet, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    # fallback: look for an em dash pattern
    match2 = re.search(r'[—–-]\s*(.+)', snippet)
    if match2:
        return match2.group(1).strip()
    return ""


def _extract_reflection(snippet: str) -> str:
    """Pull the reflection text from a <p class='reflection'> tag."""
    import re
    match = re.search(r'<p[^>]*class=["\']reflection["\'][^>]*>(.*?)</p>', snippet, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return ""


def build_email_html_raw(content_snippet: str) -> str:
    """
    Alternative builder — embeds the agent's raw HTML snippet directly
    into the card body without parsing. Use this if the agent returns
    well-structured HTML you want to preserve as-is.
    """
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Daily Inspiration</title>
</head>
<body style="margin:0; padding:0; background-color:#f0f4f8; font-family: Georgia, 'Times New Roman', serif;">

  <table width="100%" cellpadding="0" cellspacing="0" border="0"
         style="background-color:#f0f4f8; padding: 40px 20px;">
    <tr>
      <td align="center">
        <table width="600" cellpadding="0" cellspacing="0" border="0"
               style="background-color:#ffffff; border-radius:16px;
                      box-shadow: 0 4px 24px rgba(0,0,0,0.08);
                      overflow:hidden; max-width:600px;">
          <tr>
            <td align="center"
                style="background: linear-gradient(135deg, #a8c8e8 0%, #d4a8d4 100%);
                       padding: 36px 40px 28px;">
              <h1 style="margin:0; font-size:28px; color:#ffffff;
                         letter-spacing:2px; font-weight:normal;">
                ✨ Daily Inspiration ✨
              </h1>
            </td>
          </tr>
          <tr>
            <td style="padding: 40px 48px 32px;">
              {content_snippet}
            </td>
          </tr>
          <tr>
            <td align="center"
                style="background-color:#f8f4ff; padding: 24px 40px;
                       border-top: 1px solid #e8e0f0;">
              <p style="margin:0; font-size:15px; color:#9e86c8;">
                Have a wonderful day 🌷
              </p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>

</body>
</html>"""
    return html
