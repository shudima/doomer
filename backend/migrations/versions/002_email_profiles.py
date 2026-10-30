"""Remember unverified email profile labels without storing raw email addresses."""
from alembic import op
import sqlalchemy as sa

revision = '002'
down_revision = '001'
branch_labels = None
depends_on = None

def upgrade():
    schema = 'doomer' if op.get_bind().dialect.name == 'postgresql' else None
    op.create_table('email_profile',
        sa.Column('email_hash', sa.String(64), primary_key=True),
        sa.Column('user_id', sa.String(128), nullable=False, unique=True), schema=schema)

def downgrade():
    schema = 'doomer' if op.get_bind().dialect.name == 'postgresql' else None
    op.drop_table('email_profile', schema=schema)
